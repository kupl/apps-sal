from functools import reduce
from math import factorial


def value_at(poly, x):
    return round(sum(n * aCb(x, i) for i, n in enumerate(poly[::-1])), 2)


def aCb(a, b):
    return reduce(lambda x, y: x * y, (a - i for i in range(b)), 1) / factorial(b)
