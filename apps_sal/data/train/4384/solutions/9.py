import math


def fraction(a, b):
    g = math.gcd(a, b)
    return a / g + b / g
