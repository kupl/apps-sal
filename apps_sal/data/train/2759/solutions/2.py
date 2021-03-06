from itertools import chain, zip_longest


def interleave(*args):
    return [*chain.from_iterable(zip_longest(*args))]
