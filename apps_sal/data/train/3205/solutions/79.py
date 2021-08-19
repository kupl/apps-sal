import math


def is_divisible(n, x, y):
    # your code here
    a = math.trunc(n / x)
    b = math.trunc(n / y)
    return (a == n / x and b == n / y)
