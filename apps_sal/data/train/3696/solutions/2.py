from itertools import accumulate


def add(a):
    return isinstance(a, list) and all(isinstance(x, int) for x in a) and [*accumulate(a)] or "Invalid input"
