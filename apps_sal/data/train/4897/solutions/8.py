from math import gcd


def binary_gcd(x, y):
    return sum(1 for x in bin(gcd(x, y)) if x == '1')
