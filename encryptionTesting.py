import os
import time
import random
import sympy
from Crypto.Util import number
from Crypto.Util.number import inverse
from Crypto.Util.number import *


def rng(length):
    return random.getrandbits(length) | (1 << length - 1) | 1

def generate_prime_in_range(start, end):
    while True:
        p = random.randint(start, end)
        if sympy.isprime(p):
            return p


# file_name = input("Enter the file name: ")
file_name = "sampleText.txt"
# key = int(input("Enter the key value: "))
length = 2000
key = random.getrandbits(length) | (1 << length - 1) | 1
start = time.time()
# LRSA KGS
random_number_a = rng(length)
random_number_b = rng(length)

while random_number_b == random_number_a:
    random_number_b == rng(length)

product = random_number_a * random_number_b
random_prime = generate_prime_in_range(2 ** 1900, product)

m = product - random_prime
e = m + random_number_a
d = m + random_number_b
n = int(((e * d) - random_prime) // m)
q = pow(random_prime, -1, mod=n)

file_stats = os.stat(file_name)
file_size = int(file_stats.st_size)

plain_file = open(file_name, "rb+")

byte_count = -1

while byte_count != int(file_size):
    byte = plain_file.read(1)
    # print(byte) # Raw Byte data read from the file
    converted_byte = int.from_bytes(byte, "big")
    # print(converted_byte)  # Converting the raw byte data to int for encryption
    C = random.randint(0, converted_byte)
    R = converted_byte - C
    # print(converted_byte, C, R)

    # Level 1 Encryption
    CT11 = C ^ key
    CT21 = R ^ key
    # print(CT1, CT2)

    # Level 2 Encryption
    CT12 = int(pow((CT11 * e), 1, n))
    CT22 = int(pow((CT21 * d), 1, n))
    # print(CT12, CT22)

    # Writing the encrypted data to 2 different files
    encrypted_file = open("Encrypted_file1.txt", "a")
    encrypted_file.write(str(CT12) + "\n")

    encrypted_file = open("Encrypted_file2.txt", "a")
    encrypted_file.write(str(CT22) + "\n")

    byte_count += 1

end = time.time()
print("It took ", end - start, "ms to encrypt")

print("Encrypted File 1 will be saved to cloud A")
print("Encrypted File 2 will be saved to cloud B")
print("The LRSA KGS generate keys ")
print(e, d, q, n, key)

decrypt_start = time.time()
made_file = open("remade.txt", 'w+')

with open("Encrypted_file1.txt", 'r+') as f1, open("Encrypted_file2.txt", 'r+') as f2:
    C_Data = [int(line.rstrip('\n')) for line in f1]
    R_Data = [int(line.rstrip('\n')) for line in f2]

# print(len(C_Data), len(R_Data))

for i in range(len(R_Data)):
    DCT11 = int(pow((C_Data[i] * d * q), 1, n))
    DCT22 = int(pow((R_Data[i] * e * q), 1, n))

    DCT1 = DCT11 ^ key
    DCT2 = DCT22 ^ key

    message = DCT1 + DCT2
    made_file.write(chr(message))

print("It took ", time.time() - decrypt_start, "ms to decrypt")


