from itertools import groupby

def uniq(a):
    return [x for x, _ in groupby(a)]
