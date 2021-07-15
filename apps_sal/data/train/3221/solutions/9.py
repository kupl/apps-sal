from itertools import groupby

def find_it(seq):
    return next(k for k, g in groupby(sorted(seq)) if len(list(g)) % 2)

