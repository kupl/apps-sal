from itertools import chain, zip_longest

def interleave(*args):
    return [*chain(*zip_longest(*args))]
