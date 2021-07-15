from functools import reduce


def increasing_numbers(n):
    return reduce(int.__mul__, range(n + 1, n + 10)) // 362880
