from math import gcd


def reflections(x, y):
    v = gcd(x, y)
    (x, y) = (x // v, y // v)
    return not x & 1 ^ y & 1
