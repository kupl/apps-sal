from itertools import groupby


def uniq_c(seq):
    ans = []
    for c, e in groupby(seq):
        l = list(e)
        ans.append((c, len(l)))
    return ans
