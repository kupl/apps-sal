PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]


def primes():
    """Yields 'all' prime numbers"""
    yield from PRIMES

    # Last known prime
    n = PRIMES[-1]
    # Approx limit of primes that can be factors
    limit = int(n ** 0.5)
    check = limit * limit

    while True:
        # Next prime candidate for testing
        n += 2
        # Maintain limit
        if check < n:
            limit += 1
            check = limit * limit

        # Using Fundamental Theorem of Arithemtic we only need to check primes are factors to determine if composite
        for p in PRIMES:
            if n % p == 0:
                # n has a prime factor, so it is not prime
                break
            if p > limit:
                # No further primes can be a factor as the counterpart n/p would have already been found.
                # So n must be prime
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
            # Found a factor
            factors.append(p)
            while n % p == 0:
                n //= p
        elif p * p > n:
            # No need for more tests, the residual value must be prime
            factors.append(n)
            n = 1

        if n <= 1:
            # Found all prime factors
            break
    return factors


def totient(n):
    if not isinstance(n, int) or n < 1:
        return 0

    factors = prime_factors(n)
    # print(f'Prime factors of {n}: {factors}')
    if not factors:
        # Only gcd(1, 1) == 1
        return 1

    if factors[0] == n:
        # n is prime, so all gcd([1..n - 1], n) == 1
        return n - 1

    # Apply Euler's product formula to calculate totient: n * prod((f - 1) / f)
    for f in factors:
        n //= f
        n *= f - 1
    return n
