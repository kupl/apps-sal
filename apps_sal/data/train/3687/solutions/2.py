from fractions import gcd
from functools import reduce

def mn_lcm(m, n):
    m, n = sorted([m, n])
    return reduce(lambda x, y: x * y / gcd(x, y), range(m, n + 1))
