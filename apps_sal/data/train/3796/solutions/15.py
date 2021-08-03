from itertools import zip_longest


def or_arrays(*args):
    p, q, *c = args
    return [a | b for a, b in zip_longest(p, q, fillvalue=c[0] if c else 0)]
