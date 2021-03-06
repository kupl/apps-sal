from operator import mul
from functools import reduce


def factorial(n):
    if n < 0:
        return None
    return reduce(mul, range(1, n + 1), 1)
