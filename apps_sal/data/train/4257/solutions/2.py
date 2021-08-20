from math import factorial


def calculate_probability(n):
    return round(1 - factorial(365) / (factorial(365 - n) * 365 ** n) if n < 365 else 1, 2)
