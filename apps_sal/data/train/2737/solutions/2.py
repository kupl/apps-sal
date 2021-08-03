from itertools import chain


def f(t):
    return [sorted(t)] if not isinstance(t[0], list) else chain(*(f(x) for x in t))


def near_flatten(lst):
    return sorted(chain(*(f(x) for x in lst)))
