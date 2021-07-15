from math import factorial
def diagonal(n, p):
    return factorial(n + 1) // (factorial(p + 1) * factorial(n - p))
