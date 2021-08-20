from itertools import compress
import numpy as np
s = np.ones(100000)
s[:2] = s[4::2] = 0
for i in range(3, int(len(s) ** 0.5) + 1, 2):
    if s[i]:
        s[i * i::i] = 0
primes = list(compress(range(len(s)), s))


def is_prime_happy(n):
    print(n)
    i = np.searchsorted(primes, n)
    return i > 0 and sum(primes[:i]) % n == 0
