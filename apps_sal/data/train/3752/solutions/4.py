from math import factorial
from functools import lru_cache
factorial = lru_cache(maxsize=None)(factorial)


def comb(a, b):
    if isinstance(a, int):
        return int(factorial(a) / factorial(b) / factorial(max(0, a - b)))
    r = 1
    for i in range(b):
        r *= a - i
    return r / factorial(b)


def value_at(a, n):
    return round(sum((x * comb(n, i) for (i, x) in enumerate(a[::-1]))), 2)
