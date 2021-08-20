from math import sqrt


def nth_fib(n):
    n = n - 1
    Phi = (1 + sqrt(5)) / 2
    phi = (1 - sqrt(5)) / 2
    return int((Phi ** n - phi ** n) / sqrt(5))
