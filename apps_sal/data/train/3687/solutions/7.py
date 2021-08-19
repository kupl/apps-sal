from fractions import gcd
from functools import reduce


def lcm(a, b):
    return a // gcd(a, b) * b


def mn_lcm(m, n):
    (m, n) = sorted([m, n])
    return reduce(lcm, range(m, n + 1))
