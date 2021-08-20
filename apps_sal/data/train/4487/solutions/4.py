from itertools import tee


def pairwise(iterable):
    (a, b) = tee(iterable)
    next(b, None)
    return zip(a, b)


def length(value):
    try:
        return len(value)
    except TypeError:
        return len(str(value))


def order_type(values):
    if len(values) <= 1:
        return 'Constant'
    deltas = [length(b) - length(a) for (a, b) in pairwise(values)]
    min_delta = min(deltas)
    max_delta = max(deltas)
    if min_delta == max_delta == 0:
        return 'Constant'
    if min_delta >= 0 and max_delta >= 0:
        return 'Increasing'
    if min_delta <= 0 and max_delta <= 0:
        return 'Decreasing'
    return 'Unsorted'
