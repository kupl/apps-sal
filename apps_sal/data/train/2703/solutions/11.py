import functools


def square_sum(numbers):
    return functools.reduce(lambda x, y: x + y ** 2, numbers, 0)
