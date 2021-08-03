from math import fabs


def multiply(n):
    return n * (5**len(str(int(fabs(n)))))
