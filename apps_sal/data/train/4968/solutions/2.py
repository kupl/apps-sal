from math import gcd


def relatively_prime(n, lst):
    return [m for m in lst if gcd(m, n) == 1]
