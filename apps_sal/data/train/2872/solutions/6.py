import itertools


def coin(n):
    l = list(itertools.product('HT', repeat=n))
    return [''.join(list) for list in l]
