import itertools


def sum_of_n(n):
    step = +1 if n >= 0 else -1
    return list(itertools.accumulate(range(0, n + step, step)))
