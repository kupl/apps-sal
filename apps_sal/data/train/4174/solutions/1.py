from functools import reduce
from math import gcd
lcm = lambda x,y: x*y//gcd(x, y)

# Note: there is a lcm function in numpy 1.17 but codewars uses 1.14
def smallest(n):
    return reduce(lcm, range(1, n+1))
