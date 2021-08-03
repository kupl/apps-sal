from math import gcd


def reflections(x, y):
    g = gcd(x, y)
    return (x // g + y // g) % 2 == 0
