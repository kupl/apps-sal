from fractions import gcd
from statistics import mean


def gcd_matrix(xs, ys):
    return round(mean(gcd(x, y) for x in xs for y in ys), 3)
