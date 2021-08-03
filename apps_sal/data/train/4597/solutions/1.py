from itertools import chain, zip_longest


def combine(*args):
    return [x for x in chain.from_iterable(zip_longest(*args)) if x is not None]
