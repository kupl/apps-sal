from itertools import groupby


def uniq(seq):
    return [k for (k, _) in groupby(seq)]
