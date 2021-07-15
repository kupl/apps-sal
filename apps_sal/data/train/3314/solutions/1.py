from math import gcd


def solve(a, b):
    while 1 < gcd(a, b):
        b = b // gcd(a, b)
    return b == 1

