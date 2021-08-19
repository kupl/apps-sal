from itertools import groupby


def uniq_c(seq):
    return [(chr, len(list(n))) for (chr, n) in groupby(seq)]
