from math import factorial


def increasing_numbers(d):
    return factorial(9 + d) / (factorial(d) * factorial(9)) if d > 0 else 1
