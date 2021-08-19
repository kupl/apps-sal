from itertools import zip_longest


def createDict(K, V):
    return {k: v for (k, v) in zip_longest(K, V) if k}
