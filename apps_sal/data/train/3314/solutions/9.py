from math import ceil, sqrt


def factorize(x):
    factors = []
    for i in range(2, ceil(sqrt(x)) + 1):
        while x % i == 0:
            factors.append(i)
            x /= i
    if x != 1:
        factors.append(x)
    return factors


def solve(a, b):
    factors = factorize(b)
    ok = True
    for factor in factors:
        if a % factor != 0:
            ok = False
    return ok
