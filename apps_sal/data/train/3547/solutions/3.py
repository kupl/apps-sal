from collections import Counter


def odd_ones_out(a):
    d = Counter(a)
    return [x for x in a if not d[x] % 2]
