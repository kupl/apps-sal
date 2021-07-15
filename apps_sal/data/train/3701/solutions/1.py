from math import gcd
from functools import reduce
def lcm(*args):
    return reduce(lambda x,y : abs(x*y)//gcd(x,y), args) if args else 1

