from itertools import zip_longest


def hamming_distance(a, b):
    return sum((x != y for (x, y) in zip_longest(*[bin(x)[-1:1:-1] for x in (a, b)], fillvalue='0')))
