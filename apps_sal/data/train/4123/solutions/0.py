from itertools import combinations
from math import gcd


def lcm_cardinality(n):
    return 1 + sum((1 for (a, b) in combinations(divisors(n), 2) if lcm(a, b) == n))


def divisors(n):
    d = {1, n}
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            d.add(k)
            d.add(n // k)
    return sorted(d)


def lcm(a, b):
    return a * b // gcd(a, b)
