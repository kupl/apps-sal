from bisect import bisect


def sieve(n):
    sieve, primes = [0] * (n + 1), []
    for i in range(2, n + 1):
        if not sieve[i]:
            primes.append(i)
            for j in range(i**2, n + 1, i):
                sieve[j] = 1
    return primes


PRIMES = sieve(1000000)


def summationOfPrimes(n):
    return sum(PRIMES[:bisect(PRIMES, n)])
