from functools import reduce
from math import gcd

def candies_to_buy(kids):
    return reduce(lambda a, b: a * b // gcd(a, b), range(1, kids+1))
