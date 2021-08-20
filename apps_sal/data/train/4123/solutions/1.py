from math import gcd
from itertools import combinations


def divisors(n):
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            yield i
            if i * i != n:
                yield (n // i)


def lcm_cardinality(n):
    return sum((a * b == gcd(a, b) * n for (a, b) in combinations(divisors(n), 2))) + 1
