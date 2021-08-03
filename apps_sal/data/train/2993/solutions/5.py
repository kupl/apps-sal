from itertools import zip_longest


def poly_add(p1, p2):
    return list(map(sum, zip_longest(p1, p2, fillvalue=0)))
