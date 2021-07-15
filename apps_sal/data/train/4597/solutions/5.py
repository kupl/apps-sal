from itertools import zip_longest
def combine(*args):
    return [y for x in zip_longest(*args) for y in list(x) if y is not None]
