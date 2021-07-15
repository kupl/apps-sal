from collections import Counter

def prime_factors(n):
    factors = Counter()
    d = 2
    while d ** 2 <= n:
        while n % d == 0:
            n //= d
            factors[d] += 1
        d += 1 + (d > 2)
    if n > 1:
        factors[n] += 1
    return factors


def mobius(n):
    factors = prime_factors(n)
    if any(c > 1 for c in factors.values()):
        return 0
    elif sum(factors.values()) % 2 == 0:
        return 1
    return -1
