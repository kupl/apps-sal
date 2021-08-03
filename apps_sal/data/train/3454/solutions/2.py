from functools import reduce
from math import gcd


def lcm(a, b):
    g = gcd(a, b)
    return a * b // g


def candies_to_buy(kids):
    return reduce(lcm, range(1, kids + 1))
