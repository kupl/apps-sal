from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]
