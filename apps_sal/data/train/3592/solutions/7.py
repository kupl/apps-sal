from math import gcd


def lcm(x, y):
    return x // gcd(x, y) * y


def greatest(x, y, n):
    m = lcm(x, y)
    return (n - 1) // m * m


def smallest(x, y, n):
    m = lcm(x, y)
    return (n // m + 1) * m
