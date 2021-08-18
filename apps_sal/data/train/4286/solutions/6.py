from itertools import count
from bisect import bisect_left as bisect

n = 100005
sieve, primes = [0] * ((n >> 1) + 1), [2]
for i in range(3, n + 1, 2):
    if not sieve[i >> 1]:
        primes.append(i)
        for j in range(i**2 >> 1, (n + 1) >> 1, i):
            sieve[j] = 1


def solve(n):
    if n % 2 and n >> 1 < len(sieve) and not sieve[n >> 1]:
        return n

    idx = bisect(primes, n)
    return bigSearch(n, idx) if idx == len(primes) \
        else min(primes[max(0, idx - 1):idx + 2], key=lambda x: (abs(x - n), x))


def isPrime(n, iSq): return all(n % x for x in primes[:iSq])


def bigSearch(n, idx):
    iSq = bisect(primes, n**.5, 0, idx)
    isPair = not n % 2
    for x in count(0):
        for c in [-1, 1]:
            p = n + c * (2 * x + isPair)
            if isPrime(p, iSq):
                return p
