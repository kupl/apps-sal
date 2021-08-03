from bisect import bisect_left as bisect
from itertools import combinations

import numpy as np

N = 100001
xs = np.ones(N)
xs[:2] = 0
xs[2 * 2:: 2] = 0
for i in range(3, int(N ** 0.5) + 1):
    if xs[i]:
        xs[i * i:: i] = 0
primes = [i for i, x in enumerate(xs) if x]


def prime_primes(N):
    i = bisect(primes, N)
    xs = [a / b for a, b in combinations(primes[:i], 2)]
    return len(xs), int(sum(xs))
