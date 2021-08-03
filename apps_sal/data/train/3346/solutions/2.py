import numpy as np

sieve = np.ones(12_000_000, dtype=bool)
sieve[0] = sieve[1] = 0
sieve[2 * 2::2] = 0
for i in range(3, int(len(sieve)**0.5) + 1, 2):
    if sieve[i]:
        sieve[i * i::i] = 0
primes = np.array([i for i, x in enumerate(sieve) if x], dtype=int)


def gap(g, m, n):
    i = primes.searchsorted(m)
    j = primes.searchsorted(n)
    for k in range(i, j + 1):
        if primes[k + 1] - primes[k] == g:
            return list(primes[k:k + 2])
