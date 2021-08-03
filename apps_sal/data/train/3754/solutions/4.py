from itertools import compress
import numpy as np
from bisect import bisect

xs = np.ones(300000)
xs[:2] = 0
xs[4::2] = 0
for i in range(3, int(len(xs)**0.5) + 1):
    if xs[i]:
        xs[i * i::i] = 0
primes = list(compress(range(len(xs)), xs))


def iter_primes(n):
    i = bisect(primes, n // 2)
    for x in range(2, primes[i] + 1):
        if xs[x] and xs[n - x]:
            yield x, n - x


def prime_product(n):
    return max((a * b for a, b in iter_primes(n)), default=0)
