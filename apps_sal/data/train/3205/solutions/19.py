from math import gcd


def is_divisible(n, x, y):
    return not n % (x * y // gcd(x, y))
