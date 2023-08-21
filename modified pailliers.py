import os
import time
import random
import sympy
import math
from Crypto.Util import number
from Crypto.Util.number import inverse
from Crypto.Util.number import *

def modified_Pailliers():
    k = 2048
    alphaBitLength = k + 1
    aBitLength = alphaBitLength * 2
    bit_length = int(k / 2)
    mBitLength = k - 2

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
    m = number.getPrime(mBitLength)

    CT1 = pow(g, r, nsq)
    # CTB = ((pow(h, r, Nsq)) * (one + m * N)) % Nsq
    CT2 = ((pow(h, r, nsq)) * (1 + m * n)) % nsq
    CT3 = (CT1 * Q) % N

    CT4 = (CT3 * E * D) % N
    DT = ((CT2 * pow(CT4, -a, nsq) % nsq) - 1) // n
    print(m)
    print(DT)