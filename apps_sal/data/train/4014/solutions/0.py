from itertools import zip_longest


def combine_strings(*args):
    return ''.join((''.join(x) for x in zip_longest(*args, fillvalue='')))
