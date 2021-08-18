PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]


def primes():
    """Yields 'all' prime numbers"""
    yield from PRIMES

    n = PRIMES[-1]
    limit = int(n ** 0.5)
    check = limit * limit

    while True:
        n += 2
        if check < n:
            limit += 1
            check = limit * limit

        for p in PRIMES:
            if n % p == 0:
                break
            if p > limit:
                PRIMES.append(n)
                yield n
                break


def prime_factors(n):
    """Returns the prime factors of n"""
    if n < 2:
        return []
    factors = []
    for p in primes():
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
        elif p * p > n:
            factors.append(n)
            n = 1

        if n <= 1:
            break
    return factors


def totient(n):
    if not isinstance(n, int) or n < 1:
        return 0

    factors = prime_factors(n)
    if not factors:
        return 1

    if factors[0] == n:
        return n - 1

    for f in factors:
        n //= f
        n *= f - 1
    return n
