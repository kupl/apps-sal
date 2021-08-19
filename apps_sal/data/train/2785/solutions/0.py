from fractions import Decimal, gcd
from operator import mul
from functools import reduce


def lcm(a, b=1):
    return a * b // gcd(a, b)


def parameter(n):
    digits = Decimal(n).as_tuple().digits
    return lcm(sum(digits), reduce(mul, digits))
