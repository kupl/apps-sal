from itertools import zip_longest


def or_arrays(a1, a2, d=0):
    return [x | y for (x, y) in zip_longest(a1, a2, fillvalue=d)]
