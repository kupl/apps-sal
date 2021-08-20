import numpy as np
from bisect import bisect
s = np.ones(10000000)
s[:2] = s[4::2] = 0
for i in range(3, int(len(s) ** 0.5) + 1, 2):
    if s[i]:
        s[i * i::i] = 0
p = [i for (i, x) in enumerate(s) if x]


def summationOfPrimes(n):
    return sum(p[:bisect(p, n)])
