from itertools import chain, zip_longest


def alternate_sort(l):
    l = sorted(l, key=abs)
    p, n = [n for n in l if n >= 0], [n for n in l if n < 0]
    return [n for n in chain(*zip_longest(n, p)) if n is not None]
