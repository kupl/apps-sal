from math import factorial
from functools import reduce


def product(seq):
    return reduce(lambda x, y: x * y, seq) if seq else 1


def comb(x, r):
    return product([x - i for i in range(r)]) / factorial(r)


def value_at(p, x):
    result = sum((a * comb(x, i) for (i, a) in enumerate(p[::-1])))
    return result if isinstance(x, int) else round(result, 2)
