def goldbach(n):
    if n < 2:
        return []
    if n == 4:
        return [[2, 2]]
    l = n - 2
    sieve = [True] * (l // 2)
    for i in range(3, int(l**0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((l - i * i - 1) // (2 * i) + 1)
    primes = [(2 * i + 1) for i in range(1, l // 2) if sieve[i]]
    return [[p, n - p] for p in primes if (n - p) in primes and p <= (n - p)]
