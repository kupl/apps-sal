from math import factorial


def sum_arrangements(num):
    return sum((int(_) for _ in str(num))) * factorial(len(str(num)) - 1) * int('1' * len(str(num)))
