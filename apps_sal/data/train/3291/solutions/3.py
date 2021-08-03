from bisect import *

n = 10000
sieve, PRIMES = [0] * (n + 1), []
for i in range(2, n + 1):
    if not sieve[i]:
        PRIMES.append(i)
        for j in range(i**2, n + 1, i):
            sieve[j] = 1


def primes_a_p(low, high):
    subPrimes = PRIMES[bisect_left(PRIMES, low):bisect_right(PRIMES, high)]
    ans, sP = [], set(subPrimes)

    for i, p in enumerate(subPrimes):
        for q in subPrimes[i + 1:]:
            d = q - p
            prog = [p + d * n for n in range(6)]
            if set(prog) <= sP:
                ans.append(prog)
    return ans
