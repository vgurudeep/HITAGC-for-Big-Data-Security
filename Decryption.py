import os
import time
import random
import sympy
from Crypto.Util import number
from Crypto.Util.number import inverse
from Crypto.Util.number import *

CT3 = int(input("Enter CT3: "))
CT2 = int(input("Enter CT2: "))
e = int(input("Enter e: "))
d = int(input("Enter d: "))
LRSA_n = int(input("Enter LRSA_n: "))
a = int(input("Enter a: "))
q = int(input("Enter q: "))
n = int(input("Enter n"))
nsq = n*n

CT4 = (CT3 * e * d) % LRSA_n
DT = ((CT2 * pow(CT4, -a, nsq) % nsq) - 1) // n
print(f'key is : {DT}')

data1 = []

with open('Cloud1.txt', 'r+') as decrypt:
    for line in decrypt:
        data1.append(int(line.rstrip('\n')))
decrypt.close()

data2 = []

with open('Cloud2.txt', 'r+') as decrypt2:
    for line in decrypt2:
        data2.append(int(line.rstrip('\n')))
decrypt2.close()

decrypted_file = open("DECRYPTED.txt", 'w+')
for i in range(len(data2)):
    DCT11 = int(pow((data1[i] * d * q), 1, LRSA_n))
    DCT22 = int(pow((data2[i] * e * q), 1, LRSA_n))

    DCT1 = DCT11 ^ DT
    DCT2 = DCT22 ^ DT

    DCT = DCT1 + DCT2
    char = DCT.to_bytes((DCT.bit_length() + 7) // 8, byteorder='big').decode('utf-8')
    decrypted_file.write(char)
    # print(char)

decrypted_file.close()

