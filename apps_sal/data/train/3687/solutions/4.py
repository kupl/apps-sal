from fractions import gcd
from functools import reduce


def _lcm(a, b):
    return a and b and (a * b // gcd(a, b)) or 0


def lcm(*args):
    return args and reduce(_lcm, args) or 0


def mn_lcm(m, n):
    low, high = sorted((m, n))
    return lcm(*range(low, high + 1))
