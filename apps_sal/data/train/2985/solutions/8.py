from math import gcd


def reflections(x, y):
    return ((x + y) // gcd(x, y)) % 2 == 0
