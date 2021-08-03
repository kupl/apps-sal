from itertools import compress, combinations_with_replacement
import numpy as np


s = np.ones(10001)
s[:2] = s[4::2] = 0
for i in range(3, int(len(s)**0.5) + 1, 2):
    if s[i]:
        s[i * i::i] = 0
PRIMES = list(compress(list(range(len(s))), s))


def solve(a, b):
    i, j = np.searchsorted(PRIMES, a), np.searchsorted(PRIMES, b)
    return sum(s[sum(map(int, str(x * y)))] for x, y in combinations_with_replacement(PRIMES[i:j], 2))
