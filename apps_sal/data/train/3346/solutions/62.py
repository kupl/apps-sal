def gap(g, m, n):
    primes = []
    sieve = [True] * (n + 1)
    for i in range(3, int((n + 1)**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i]=[False] * ((n - i * i) // (2 * i) + 1)
    if m % 2 == 0:
        primes = [i for i in range(m + 1, n + 1, 2) if sieve[i]]
    else:
        primes = [i for i in range(m, n + 1, 2) if sieve[i]]
    for k in range(0, len(primes) - 1):
        if primes[k + 1] - primes[k] == g:
            return [primes[k], primes[k + 1]]
    return None

