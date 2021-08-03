from collections import Counter
from math import ceil

PRIMES = [2] + [n for n in range(3, 1000, 2) if all(n % d for d in range(3, int(n**0.5) + 1, 2))]


def get_factors(n):
    factors = []
    for p in PRIMES:
        if p > n:
            break
        while n % p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        factors.append(n)
    return Counter(factors)


def mul_power(n, k):
    factors, lcm = get_factors(n), 1
    for p, e in factors.items():
        lcm *= p**(ceil(e / k) * k)
    return lcm // n
