# import random
# import math
# import sys
# import time
#
#
# def rabinMiller(n):
#     s = n - 1
#     t = 0
#     while s & 1 == 0:
#         s = s // 2
#         t += 1
#     k = 0
#     while k < 128:
#         a = random.randrange(2, n - 1)
#         # a^s is computationally infeasible.  we need a more intelligent approach
#         # v = (a**s)%n
#         # python's core math module can do modular exponentiation
#         v = pow(a, s, n)  # where values are (num,exp,mod)
#         if v != 1:
#             i = 0
#             while v != (n - 1):
#                 if i == t - 1:
#                     return False
#                 else:
#                     i = i + 1
#                     v = (v ** 2) % n
#         k += 2
#     return True
#
#
# def isPrime(n):
#     # lowPrimes is all primes (sans 2, which is covered by the bitwise and operator)
#     # under 1000. taking n modulo each lowPrime allows us to remove a huge chunk
#     # of composite numbers from our potential pool without resorting to Rabin-Miller
#     lowPrimes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
#         , 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179
#         , 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269
#         , 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367
#         , 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461
#         , 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571
#         , 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661
#         , 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773
#         , 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883
#         , 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
#     if n >= 3:
#         if n & 1 != 0:
#             for p in lowPrimes:
#                 if n == p:
#                     return True
#                 if n % p == 0:
#                     return False
#             return rabinMiller(n)
#     return False
#
#
# def generateLargePrime(k):
#     # k is the desired bit length
#     r = 100 * (math.log(k, 2) + 1)  # number of attempts max
#     r_ = r
#     while r > 0:
#         # randrange is mersenne twister and is completely deterministic
#         # unusable for serious crypto purposes
#         n = random.randrange(2 ** (k - 1), 2 ** (k))
#         r -= 1
#         if isPrime(n):
#             return n
#     return "Failure after " + repr(r_) + " tries."
#
#
# start = time.time()
# print(generateLargePrime(2048))
# print(time.time() - start)
#
import random
import sympy


# def generate_prime_in_range(start, end):
#     while True:
#         p = random.randint(start, end)
#         if sympy.isprime(p):
#             return p
#
#
# start = 2**2047 # start of range
# end = 2**2048  # end of range
# prime = generate_prime_in_range(start, end)
# print(prime)

import os

# file_name = "1MB_Size.txt"
# file_stats = os.stat(file_name)
# file_size = int(file_stats.st_size)
#
# plain_file = open(file_name, "rb+")
# made_file = open("remade.txt", 'w+')
# byte_count = -1
# while byte_count != int(file_size):
#     byte = plain_file.read(1)
#     # print(byte) # Raw Byte data read from the file
#     converted_byte = int.from_bytes(byte, "big")
#     made_file.write((str(converted_byte)))
#     byte_count += 1
import sys
# input_file = '1MB_Size.txt'
# output_file = 'output_file.txt'
# chunk_size = 1024  # Size of each chunk in bytes
#
# with open(input_file, 'r') as f_in:
#     with open(output_file, 'w') as f_out:
#         for line in f_in:
#             # Convert text to int
#             int_line = int.from_bytes(line.encode(), byteorder='big')
#             f_out.write(str(int_line))
#             # Convert int back to text
#             new_line = int_line.to_bytes((int_line.bit_length() + 7) // 8, byteorder='big').decode()
#

# import os
#
# # Define the key
# key = os.urandom(256)  # Use a 2k-bit key (256 bytes)
#
# # Open the input and output files
# with open('sampleText.txt', 'rb') as f_in, open('output_file.enc', 'wb') as f_out:
#     # Read and encrypt the input file in blocks
#     while True:
#         block = f_in.read(256)
#         int_block = int.from_bytes(block, "big")
#         print(int_block)
#         if not block:
#             break
#         # ciphertext_block = (map(lambda a, b: a ^ b, int_block, key))
#         # f_out.write(ciphertext_block)
import os

# Define the chunk size
# chunk_size = 256
# made_file = open("another.txt", 'w+')
# # Open the input file
# with open('sampleText.txt', 'rb') as f_in:
#     while True:
#         # Read the input file in chunks
#         chunk = f_in.read(chunk_size)
#         if not chunk:
#             break
#
#         # Pad the last block with spaces if it is less than chunk_size
#         if len(chunk) < chunk_size:
#             chunk += b' ' * (chunk_size - len(chunk))
#
#         # Convert the chunk into a single integer
#         int_value = int.from_bytes(chunk, byteorder='big')
#         print(int_value)
#         new_int_value = int_value ^ 102343
#         print(new_int_value)
#         retracted = new_int_value ^ 102343
#         print(retracted)
#         # Convert the integer value back to its original character representation
#         chunk_chars = retracted.to_bytes((retracted.bit_length() + 7) // 8, byteorder='big').decode('utf-8')
#         made_file.write(chunk_chars)

message = "Hello this is gurudeep testing this output"
file_name = "text.txt"
chunk_size = 256
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