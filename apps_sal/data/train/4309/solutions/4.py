from itertools import groupby
from collections import defaultdict

def replace(s):
    res, D = [], {'!':defaultdict(list), '?':defaultdict(list)}
    for i, (k, l) in enumerate(groupby(s)):
        s = len(list(l))
        D[k][s].append(i)
        res.append([k, s])
    for v, L1 in D['!'].items():
        L2 = D['?'][v]
        while L1 and L2:
            res[L1.pop(0)][0] = ' '
            res[L2.pop(0)][0] = ' '
    return ''.join(c*v for c,v in res)
