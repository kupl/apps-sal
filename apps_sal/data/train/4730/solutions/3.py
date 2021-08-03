from itertools import compress
import numpy as np

s = np.ones(200001)
s[:2] = s[4::2] = 0
for i in range(3, int(len(s)**0.5) + 1, 2):
    if s[i]:
        s[i * i::i] = 0
primes = list(compress(range(len(s)), s))


def prime_bef_aft(num):
    i = np.searchsorted(primes, num)
    return [primes[i - 1], primes[i + (primes[i] == num)]]
