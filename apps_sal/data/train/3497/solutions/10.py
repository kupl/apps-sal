import math


def isPP(n):
    return next(([b, round(math.log(n, b))] for b in range(2, int(n**0.5) + 1) if b**round(math.log(n, b)) == n), None)
