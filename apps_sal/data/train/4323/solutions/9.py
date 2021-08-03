from itertools import groupby


def uniq(seq):
    return [k[0] for k in groupby(seq)]
