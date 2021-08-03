from fractions import gcd


def binary_gcd(x, y):
    return bin(gcd(x, y)).count('1')
