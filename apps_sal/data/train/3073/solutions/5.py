from math import factorial


def nCr(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)


def increasing_numbers(digits):
    return nCr(digits + 9, 9)
