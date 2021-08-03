from itertools import chain, zip_longest


def combine_strings(*args):
    return ''.join(chain.from_iterable(zip_longest(*args, fillvalue='')))
