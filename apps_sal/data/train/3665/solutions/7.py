import numpy as np

xs = np.zeros(20001)
xs[:2] = xs[2 * 2::2] = 1
for i in range(3, int(len(xs)**0.5) + 1, 2):
    xs[i * i::i] = 1
n_primes = np.array([i for i in range(1, 20001) if xs[i] and all(c in '2357' for c in str(i))], dtype=int)


def not_primes(a, b):
    return n_primes[np.searchsorted(n_primes, a):np.searchsorted(n_primes, b)].tolist()
