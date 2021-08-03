from operator import lt, gt
from itertools import combinations as c


def longest_comb(a, s):
    o = lt if s in '< <<' else gt
    for k in xrange(len(a) - 1, 2, -1):
        r = []
        for x in c(a, k):
            if all(o(x[i - 1], e) if i else True for i, e in enumerate(x)):
                r += [list(x)]
        if len(r):
            return r if len(r) > 1 else r[0]
    return []
