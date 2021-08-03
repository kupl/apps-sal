from functools import reduce


def sum_of_minimums(numbers):
    return reduce(lambda x, y: min(y) + x, numbers, 0)
