import functools


def sum_of_intervals(intervals):
    return len(functools.reduce(lambda x, y: x | y, [set(range(x, y)) for (x, y) in intervals]))
