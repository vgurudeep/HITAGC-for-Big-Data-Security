import random
import time
import os


def prime_number_generator(max_int_limit, max_bit_limit):
    possible_range = []

    if max_int_limit == 0:
        n = 2 ** max_bit_limit + 1
    elif max_bit_limit == 0:
        n = max_int_limit + 1

    for i in range((n)):
        possible_range.append(i)

    possible_range[0] = 0
    possible_range[1] = 0
    p = 2

    while p * p <= 2 ** bits:
        if p != 0:
            for i in range(p * 2, n, p):
                possible_range[i] = 0
        p += 1

    prime_list = list(filter(lambda x: x != 0, possible_range))
    return prime_list


bits = int(int(input("Enter the bit length")) / 2)

primes_in_K_bit_range = prime_number_generator(0, bits)

p = random.choice(primes_in_K_bit_range)
q = random.choice(primes_in_K_bit_range)

while q == p:
    q = random.choice(primes_in_K_bit_range)

n = p * q
nSquare = n * n

primes_in_n_range = prime_number_generator(n, 0)
alpha = random.choice(primes_in_n_range)

primes_in_nSquare_range = prime_number_generator(nSquare, 0)
a = random.choice(primes_in_nSquare_range)

# print(p, q, n, nSquare, alpha, a)


def gcd(a, h):
    temp = 0
    while (1):
        temp = a % h
        if temp == 0:
            return h
        a = h
        h = temp


g = 2

while g < nSquare:
    if gcd(g, nSquare) == 1:
        break
    else:
        g = g + 1

print("g is ", g)

alphaSquare = (alpha*alpha)*pow((1, nSquare))
print(alphaSquare, g)
