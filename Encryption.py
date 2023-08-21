import os
import time
import random
import sympy
from Crypto.Util import number
from Crypto.Util.number import inverse
from Crypto.Util.number import *

k = 2048


# key = number.getPrime(k)

def rng(length):
    return random.getrandbits(length) | (1 << length - 1) | 1


# Function to generate a random prime number in a given range
def generate_prime_in_range(start, end):
    while True:
        p = random.randint(start, end)
        if sympy.isprime(p):
            return p


start = time.time()
# Linear RSA key generation
random_number_a = rng(k)
random_number_b = rng(k)
while random_number_b == random_number_a:
    random_number_b == rng(k)

product = random_number_a * random_number_b

random_prime = generate_prime_in_range(1, product)

m = product - random_prime
e = m + random_number_a
d = m + random_number_b
LRSA_n = int(((e * d) - random_prime) // m)
Q = pow(random_prime, -1, mod=LRSA_n)

# Modified Paillier`s
alphaBitLength = k + 1
aBitLength = alphaBitLength * 2
bit_length = int(k / 2)
mBitLength = k - 2

# Generating 2 unique prime numbers..
p = number.getPrime(bit_length)
q = number.getPrime(bit_length)
while p == q:
    q = number.getPrime(bit_length)

n = p * q
nsq = n ** 2

alpha = number.getPrime(alphaBitLength)
a = number.getPrime(aBitLength)

alphasq = (alpha ** 2) % nsq
lambda_val = ((p - 1) * (q - 1)) // (number.GCD(p - 1, q - 1))
# lambda_val = math.lcm(p-1, q-1)
ordG = n * lambda_val // 2
g = alphasq % nsq

h = pow(g, a, nsq)
# Compute the modular inverse of g modulo Nsq
# g_inv = inverse(g, nsq)  # optional

# M = nsq - p
# E = M + n
# D = M + n
# N = M + (2 * n) + 1
# Q = pow(p, -1, mod=N)

r = random.getrandbits(bit_length) | (1 << bit_length - 1) | 1
key = number.getPrime(mBitLength)

# Encrypting the key ( output`s CT2 and CT3 )
CT1 = pow(g, r, nsq)
# CTB = ((pow(h, r, Nsq)) * (one + m * N)) % Nsq
CT2 = ((pow(h, r, nsq)) * (1 + key * n)) % nsq
CT3 = (CT1 * Q) % LRSA_n
end = time.time() - start
with open("Encrypted_keys.txt", 'w+') as file:
    file.write(f"CT2: {CT2} \n")
    file.write(f"CT3: {CT3}")
file.close()

with open("Public_Keys.txt", 'w+') as file1:
    file1.write(f"m: {m}\n")
    file1.write(f"n: {n}\n")
    file1.write(f"Q: {Q}\n")
    file1.write(f"g: {g}\n")
    file1.write(f"LRSA_n: {LRSA_n}\n")
    file1.write(f"h: {h}")
file1.close()

with open("Private_Keys.txt", 'w+') as file2:
    file2.write(f"a: {a}\n")
    file2.write(f"e: {e}\n")
    file2.write(f"d: {d}\n")
    file2.write(f"n: {n}\n")
    file2.write(f"Q: {Q}\n")
    file2.write(f"LRSA_n: {LRSA_n}\n")
    file2.write(f"nsq: {nsq}")
file2.close()

print("Public keys are :")
print("m: ", m)
print("n: ", n)
print("Q: ", Q)
print("g: ", g)
print("LRSA_N: ", LRSA_n)
print("h: ", h)

print("Private keys are: ")
print("a: ", a)
print("e: ", e)
print("d: ", d)
print("n: ", n)
print("LRSA_N: ", LRSA_n)

print("Cipher texts are :")
print("CT2: ", CT2)
print("CT3: ", CT3)

print(f'Total time taken for key Generation is : {end}')

chunk_size = 256
#
file_name = 'hello.txt'
enc_time = time.time()
# Open the input file
with open(file_name, 'rb') as f_in, open("Cloud1.txt", 'w+') as made_file, open("Cloud2.txt", 'w+') as made_file1:
    while True:
        # Read the input file in chunks
        chunk = f_in.read(chunk_size)
        if not chunk:
            break

        # Pad the last block with spaces if it is less than chunk_size
        if len(chunk) < chunk_size:
            chunk += b' ' * (chunk_size - len(chunk))

        # Convert the chunk into a single integer
        int_value = int.from_bytes(chunk, byteorder='big')
        C = random.randint(1, int_value)
        R = int_value - C

        CT01 = C ^ key
        CT02 = R ^ key

        CT1 = int(pow((CT01 * e), 1, LRSA_n))
        CT2 = int(pow((CT02 * d), 1, LRSA_n))

        # Convert the integer value back to its original character representation
        # chunk_chars = retracted.to_bytes((retracted.bit_length() + 7) // 8, byteorder='big').decode('utf-8')

        made_file.write(str(CT1) + "\n")
        made_file1.write(str(CT2) + "\n")

f_in.close()
made_file.close()
made_file1.close()
print(f'Time taken to encrypt the files: {time.time()-enc_time} seconds')

