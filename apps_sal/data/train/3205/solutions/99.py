from math import gcd


def is_divisible(n, x, y):
    return True if n // (x * y / gcd(x, y)) == n / (x * y / gcd(x, y)) else False
