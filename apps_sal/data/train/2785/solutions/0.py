from fractions import Decimal, gcd
from operator import mul
from functools import reduce

lcm = lambda a, b=1: a * b // gcd(a, b)

def parameter(n):
    digits = Decimal(n).as_tuple().digits
    return lcm(sum(digits), reduce(mul, digits))
