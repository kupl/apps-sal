from bisect import bisect_left as bisect

base, n = set("2357"), 20000
sieve = [1, 0] * ((n >> 1) + 1)
sieve[2] = 0
for i in range(3, n + 1, 2):
    if not sieve[i]:
        for j in range(i**2, n + 1, i):
            sieve[j] = 1

NOT_PRIMES = [x for x in range(n) if sieve[x] and not (set(str(x)) - base)]


def not_primes(a, b):
    end = bisect(NOT_PRIMES, b)
    return NOT_PRIMES[bisect(NOT_PRIMES, a, 0, end): end]
