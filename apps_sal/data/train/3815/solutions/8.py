from fractions import gcd as g


def z(x, y):
    return 1 if g(x, y) == 1 else 0


def coprimes(n):
    return [i for i in range(1, n) if z(n, i) == 1]
