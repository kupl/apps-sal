from itertools import compress
from math import log
import numpy as np

n = 1_500_000
s = np.ones(n, dtype=int)
s[:2] = s[4::2] = 0
for i in range(3, int(len(s)**0.5) + 1, 2):
    if s[i]:
        s[i * i::i] = 0
ps = set(compress(range(len(s)), s))
stone_bridge_primes = set()
for i in range(int(log(n, 2)) + 1):
    for j in range(int(log(n, 3)) + 1):
        x = 2**i * 3**j + 1
        if x in ps:
            stone_bridge_primes.add(x)
sbp = sorted(stone_bridge_primes)


def solve(x, y):
    return np.searchsorted(sbp, y) - np.searchsorted(sbp, x)
