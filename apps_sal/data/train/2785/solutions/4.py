from fractions import gcd
from functools import reduce
from operator import mul

def parameter(n):
    digits = [int(d) for d in str(n)]
    product = reduce(mul, digits)
    total = sum(digits)
    return product * total / gcd(product, total)
