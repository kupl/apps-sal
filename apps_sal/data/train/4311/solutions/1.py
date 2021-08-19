from bisect import bisect_left


def sieve(n):
    (sieve, primes) = ([0] * (n + 1), [])
    for i in range(2, n + 1):
        if not sieve[i]:
            primes.append(i)
            for j in range(i ** 2, n + 1, i):
                sieve[j] = 1
    return primes


PRIMES = sieve(10000)
SET_PRIMES = set(PRIMES)


def solve(a, b):
    (p1, p2) = (bisect_left(PRIMES, a), bisect_left(PRIMES, b))
    return sum((sum(map(int, str(p * q))) in SET_PRIMES for (i, p) in enumerate(PRIMES[p1:p2], p1) for q in PRIMES[i:p2]))
