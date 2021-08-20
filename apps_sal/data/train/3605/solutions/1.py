import math


def diagonal(n, p):
    s = 0
    f = math.factorial(p)
    for i in range(n + 1 - p):
        prod = 1
        for j in range(1, p + 1):
            prod *= i + j
        prod = prod // f
        s += prod
    return int(s)
