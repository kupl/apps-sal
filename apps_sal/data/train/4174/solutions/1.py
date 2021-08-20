from functools import reduce
from math import gcd


def lcm(x, y):
    return x * y // gcd(x, y)


def smallest(n):
    return reduce(lcm, range(1, n + 1))
