import math


def sum_digits(n):
    n = round(math.fabs(n))
    all = [int(s) for s in str(n)]
    return sum(all)
