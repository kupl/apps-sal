from math import factorial


def routes(n):
    return n > 0 and factorial(2 * n) // factorial(n)**2
