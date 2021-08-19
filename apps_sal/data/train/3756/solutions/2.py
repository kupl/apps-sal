from itertools import chain
import numpy as np
N = 32001
xs = np.ones(N)
xs[:2] = 0
xs[4::2] = 0
for i in range(3, int(N ** 0.5) + 1, 2):
    if xs[i]:
        xs[i * i::i] = 0
primes = {i for (i, x) in enumerate(xs) if x}


def goldbach_partitions(n):
    if n % 2:
        return []
    return [f'{i}+{n - i}' for i in chain([2], range(3, n // 2 + 1, 2)) if i in primes and n - i in primes]
