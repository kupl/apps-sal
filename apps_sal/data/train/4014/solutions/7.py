import itertools as it


def combine_strings(*argv):
    return ''.join(it.chain(*it.zip_longest(*argv, fillvalue='')))
