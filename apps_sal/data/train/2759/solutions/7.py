from itertools import zip_longest


def interleave(*args):
    return [i for _ in zip_longest(*args) for i in _]
