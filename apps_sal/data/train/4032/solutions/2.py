from math import factorial


def solve(n):
    return factorial(2 * n) // (factorial(n) * factorial(n + 1))
