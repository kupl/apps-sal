def sieve(n):
    (sieve, primes) = ([0] * (n + 1), set())
    for i in range(2, n + 1):
        if not sieve[i]:
            primes.add(i)
            for j in range(i ** 2, n + 1, i):
                sieve[j] = 1
    return primes


PRIMES = sieve(5000)


def total(arr):
    return sum((arr[p] for p in set(range(len(arr))) & PRIMES))
