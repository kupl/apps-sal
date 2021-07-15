from functools import reduce


def find_difference(a: list, b: list) -> int:
    return abs(reduce(lambda x, y: x * y, a) - reduce(lambda x, y: x * y, b))
