from itertools import zip_longest, chain


def sel_reverse(arr, l):
    if l == 0:
        return arr
    return [e for e in chain.from_iterable(t[::-1] for t in zip_longest(*[iter(arr)] * l)) if e is not None]
