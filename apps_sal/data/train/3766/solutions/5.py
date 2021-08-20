from collections import Counter
LIMIT = 10 ** 6
sieve = [True] * (LIMIT // 2)
for i in range(3, int(LIMIT ** 0.5) + 1, 2):
    if sieve[i // 2]:
        sieve[i * i // 2::i] = [False] * ((LIMIT - i * i - 1) // 2 // i + 1)
PRIMES = [2] + [2 * i + 1 for i in range(1, LIMIT // 2) if sieve[i]]


def getAllPrimeFactors(n):
    if not type(n) == int or n < 1:
        return []
    if n in (1, 2):
        return [n]
    factors = []
    for p in PRIMES:
        if p * p > n:
            break
        while n % p == 0:
            n //= p
            factors.append(p)
    return factors + [n] * (n > 1)


def getUniquePrimeFactorsWithCount(n):
    factors = Counter(getAllPrimeFactors(n))
    return [list(factors.keys()), list(factors.values())]


def getUniquePrimeFactorsWithProducts(n):
    factors = Counter(getAllPrimeFactors(n))
    return [p ** e for (p, e) in factors.items()]
