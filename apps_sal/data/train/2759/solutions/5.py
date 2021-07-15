from itertools import zip_longest

def interleave(*args):
    return [y for x in zip_longest(*args) for y in x]

