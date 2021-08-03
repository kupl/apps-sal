from math import factorial as f


def calculate_probability(n):
    a = 1
    for x in range(n):
        a *= (365 - x) / 365
    return round(1 - a, 2)
