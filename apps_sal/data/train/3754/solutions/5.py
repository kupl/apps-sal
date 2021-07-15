def prime_product(n, sieve=[False, False, True, True]):
    for x in range(len(sieve), n+1):
        sieve.append(x % 2 and all(x % p for p in range(3, int(x ** .5) + 1, 2) if sieve[p]))
    return next((p * (n - p) for p in range(n//2, 1, -1) if sieve[p] and sieve[n - p]), 0)
