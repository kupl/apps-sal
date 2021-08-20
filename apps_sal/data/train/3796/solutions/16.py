from itertools import starmap, zip_longest


def or_arrays(a1, a2, f=0):
    return list(starmap(int.__or__, zip_longest(a1, a2, fillvalue=f)))
