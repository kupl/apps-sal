from math import gcd
from functools import reduce

lcm = lambda x,y: x*y//gcd(x,y)

def candies_to_buy(n):
    return reduce(lcm, (i for i in range(1,(n+1 if n%2 else n)))) if n!=2 else 2
