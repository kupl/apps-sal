# generate primes
from bisect import bisect
LIMIT = 100000
sieve = [True] * (LIMIT // 2)
for n in range(3, int(LIMIT**0.5) + 1, 2):
    if sieve[n // 2]:
        sieve[n * n // 2::n] = [False] * ((LIMIT - n * n - 1) // 2 // n + 1)
PRIMES_LIST = [2] + [2 * i + 1 for i in range(1, LIMIT // 2) if sieve[i]]
PRIMES = set(PRIMES_LIST)
del sieve


def prime_product(n):
    if n % 2:
        return 2 * (n - 2) if n - 2 in PRIMES else 0

    for p in PRIMES_LIST[:bisect(PRIMES_LIST, n // 2)][::-1]:
        if n - p in PRIMES:
            return (n - p) * p
