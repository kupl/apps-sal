LIMIT = 10 ** 6
sieve = [True] * (LIMIT // 2)
for n in range(3, int(LIMIT ** 0.5) + 1, 2):
    if sieve[n // 2]:
        sieve[n * n // 2::n] = [False] * ((LIMIT - n * n - 1) // 2 // n + 1)
PRIMES = [2] + [2 * i + 1 for i in range(1, LIMIT // 2) if sieve[i]]
del sieve


def mobius(n):
    factors = []
    for p in PRIMES:
        if p * p > n:
            factors.append(n)
            break
        while n % p == 0:
            if p in factors:
                return 0
            factors.append(p)
            n //= p
        if n == 1:
            break
    return -1 if len(factors) % 2 else 1
