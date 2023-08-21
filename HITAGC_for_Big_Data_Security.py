import os
import time
import random
import sympy
from Crypto.Util import number
from Crypto.Util.number import inverse
from Crypto.Util.number import *
import chardet

# Modified Paillier`s

# Calculating Bit Length for generating keys...
k = 8  # we can take the input of this
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
g_inv = inverse(g, nsq)  # optional

M = nsq - p
E = M + n
D = M + n
N = M + (2 * n) + 1
Q = pow(p, -1, mod=N)

r = random.getrandbits(bit_length) | (1 << bit_length - 1) | 1
key = number.getPrime(mBitLength)
print(key)

# Encrypting the key ( output`s CT2 and CT3 )
CT1 = pow(g, r, nsq)
# CTB = ((pow(h, r, Nsq)) * (one + m * N)) % Nsq
CT2 = ((pow(h, r, nsq)) * (1 + key * n)) % nsq
CT3 = (CT1 * Q) % N

# Decrypting the key ( output`s DT )
CT4 = (CT3 * E * D) % N
DT = ((CT2 * pow(CT4, -a, nsq) % nsq) - 1) // n


# Function to generate a random number of given Bit length
def rng(length):
    return random.getrandbits(length) | (1 << length - 1) | 1


# Function to generate a random prime number in a given range
def generate_prime_in_range(start, end):
    while True:
        p = random.randint(start, end)
        if sympy.isprime(p):
            return p


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
q = pow(random_prime, -1, mod=LRSA_n)
# Now all the keys are generated for encryption ....


file_name = "testing time.txt"  # Take file input
file_stats = os.stat(file_name)
file_size = int(file_stats.st_size)

# Define the chunk size ( We are basically reading the file in 256 bytes of chunks )
chunk_size = 256
# Open the input file

with open(file_name, 'rb') as f_in:
    while True:
        # Read the input file in chunks
        chunk = f_in.read(chunk_size)
        if not chunk:
            break
        # Pad the last block with spaces if it is less than chunk_size
        if len(chunk) < chunk_size:
            chunk += b' ' * (chunk_size - len(chunk))
        # Convert the chunk into a single integer
        converted_byte = int.from_bytes(chunk, byteorder='big')

        C = random.randint(0, converted_byte)

        R = converted_byte - C

        # print(converted_byte, C, R)
        print("C",C)

        # Level 1 Encryption
        CT11 = C ^ key
        CT21 = R ^ key
        print("CT1",CT1)

        # Level 2 Encryption
        CT12 = int(pow((CT11 * e), 1, LRSA_n))
        CT22 = int(pow((CT21 * d), 1, LRSA_n))
        # print(CT12, CT22)

        # Writing the encrypted data to 2 different files
        encrypted_file1 = open("Encrypt_file1.txt", "w+")
        encrypted_file1.write(str(CT12) + "\n")
        encrypted_file1.close()

        encrypted_file2 = open("Encrypt_file2.txt", "w+")
        encrypted_file2.write(str(CT22) + "\n")
        encrypted_file2.close()
f_in.close()
# Encryption done...
print(key == DT)
# Decryption starts here...
made_file = open("remade.txt", 'w+') # file to save the decrypted data

with open("Encrypt_file1.txt", 'r+') as f1, open("Encrypt_file2.txt", 'r+') as f2:
    C_Data = [int(line.rstrip('\n')) for line in f1]
    R_Data = [int(line.rstrip('\n')) for line in f2]


for i in range(len(R_Data)):
    DCT11 = int(pow((C_Data[i] * d * q), 1, LRSA_n))
    DCT22 = int(pow((R_Data[i] * e * q), 1, LRSA_n))

    DCT1 = DCT11 ^ DT

    DCT2 = DCT22 ^ DT

    message = DCT1 + DCT2

    chunk_chars = message.to_bytes((message.bit_length() + 7) // 8, byteorder='big').decode('utf-8')
    made_file.write(chunk_chars)

