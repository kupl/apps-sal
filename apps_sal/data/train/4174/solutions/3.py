from functools import reduce
from math import gcd


def smallest(n):
    return reduce(lambda a, b: a * b // gcd(a, b), range(1, n + 1))
