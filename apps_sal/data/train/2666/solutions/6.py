from functools import reduce


def spacey(array):
    return reduce(lambda a, b: a + [a[-1] + b] if a else [b], array, [])
