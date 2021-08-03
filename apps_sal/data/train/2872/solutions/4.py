from itertools import product


def coin(n):
    return [''.join(p) for p in product('HT', repeat=n)]
