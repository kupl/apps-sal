from math import gcd


def reduce_fraction(fraction):
    numerator, denominator = fraction
    d = gcd(numerator, denominator)
    return (numerator // d, denominator // d)
