from itertools import chain


def unite_unique(*args):
    return list(dict.fromkeys(chain.from_iterable(args)))
