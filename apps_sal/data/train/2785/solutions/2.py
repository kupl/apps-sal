from functools import reduce
from fractions import gcd
def parameter(n):
    n = [int(i) for i in str(n)]
    sum_ = reduce(lambda a, b: a + b, n)
    prod = reduce(lambda a, b: a * b, n)
    return (sum_ * prod) / gcd(sum_, prod)
