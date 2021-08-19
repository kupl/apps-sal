from math import gcd


def gcd_matrix(a, b):
    return round(sum((gcd(m, n) for m in a for n in b)) / (len(a) * len(b)), 3)
