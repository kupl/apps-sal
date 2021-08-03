from math import factorial


def generate_diagonal(n, l):
    return [factorial(n + i) // (factorial(n) * factorial(i)) for i in range(l)]
