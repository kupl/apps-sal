def primes_set():
    primes, sieve = {2}, [True] * 50000
    for i in range(3, 317, 2):
        if sieve[i // 2]:
            sieve[i * i // 2:: i] = [False] * ((100000 - i * i - 1) // (2 * i) + 1)
    primes.update((2 * i + 1) for i in range(1, 50000) if sieve[i])
    return primes


primes = primes_set()


def prime_product(n):
    if n % 2 or n == 4:
        return (2 * (n - 2)) if (n - 2) in primes else 0
    m, s = n // 2, n % 4 == 0
    return next(((m + i) * (m - i) for i in range(s, m, 2) if {m + i, m - i} < primes), 0)
