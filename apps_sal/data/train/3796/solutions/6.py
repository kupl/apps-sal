from itertools import zip_longest


def or_arrays(a, b, filler=0):
    return [x | y for (x, y) in zip_longest(a, b, fillvalue=filler)]
