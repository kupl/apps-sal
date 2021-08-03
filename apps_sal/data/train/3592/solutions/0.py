from math import gcd


def greatest(x, y, n):
    z = x * y // gcd(x, y)
    return (n - 1) // z * z


def smallest(x, y, n):
    z = x * y // gcd(x, y)
    return (n + z) // z * z
