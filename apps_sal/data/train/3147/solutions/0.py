import numpy as np
from itertools import accumulate
def sieve_primes(n):
    sieve = np.ones(n // 2, dtype = np.bool)
    limit = 1 + int(n ** 0.5)

    for a in range(3, limit, 2):
        if sieve[a // 2]:
            sieve[a * a // 2::a] = False

    prime_indexes = 2 * np.nonzero(sieve)[0].astype(int) + 1
    prime_indexes[0] = 2
    return set(map(str, prime_indexes))

primes = sieve_primes(10 ** 6)

def all_primes(s):
    if int(s) < 10:
        return s in primes
    for n in accumulate(s[:-1]):
        if n in primes:
            m = s[len(n):]
            if m in primes or all_primes(m):
                return True

def total_primes(a, b):
    return [int(a) for a in map(str, range(max(10, a), b + 1)) if a in primes and all_primes(a)]
