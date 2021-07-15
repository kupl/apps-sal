from fractions import gcd
from functools import reduce

def candies_to_buy(n):
    return reduce(lambda a,b:a*b//gcd(a,b), range(1,n+1))
