from math import gcd


def fraction(a, b):
    return a / gcd(a, b) + b / (gcd(a, b))
