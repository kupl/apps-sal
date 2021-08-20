import numpy as np
N = 100001
s = np.ones(N)
s[:2] = 0
s[2 * 2::2] = 0
for i in range(3, int(N ** 0.5) + 1):
    if s[i]:
        s[i * i::i] = 0
primes = {i for (i, x) in enumerate(s) if x}


def goldbach(n):
    if n == 4:
        return [[2, 2]]
    return [[i, n - i] for i in range(3, n // 2 + 1, 2) if i in primes and n - i in primes]
