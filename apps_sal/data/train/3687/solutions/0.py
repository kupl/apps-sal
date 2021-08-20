from fractions import gcd
from functools import reduce


def mn_lcm(m, n):
    return reduce(lambda x, y: x * y / gcd(x, y), list(range(min(m, n), max(m, n) + 1)))
