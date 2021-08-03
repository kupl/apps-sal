from math import gcd


def reduce_fraction(fraction):
    g = gcd(*fraction)
    return tuple(n // g for n in fraction)
