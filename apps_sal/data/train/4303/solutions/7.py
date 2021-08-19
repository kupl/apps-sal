from math import factorial


def sum_arrangements(num):
    ns = list(map(int, str(num)))
    mul = factorial(len(ns) - 1)
    return int('1' * len(ns)) * sum(ns) * mul
