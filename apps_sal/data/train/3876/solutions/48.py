from functools import reduce


def find(n):
    return reduce(lambda x, y: x + y if y % 3 == 0 or y % 5 == 0 else x, list(range(n + 1)), 0)
