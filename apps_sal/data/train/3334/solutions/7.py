from math import gcd


def reduce_fraction(fraction):
    a, b = fraction
    g = gcd(a, b)
    return (a // g, b // g)
