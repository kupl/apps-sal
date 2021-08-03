from fractions import gcd
from functools import reduce


def lcm(a, b):
    return a * b // gcd(a, b)


def candies_to_buy(amount_of_kids_invited):
    return reduce(lcm, range(1, amount_of_kids_invited + 1))
