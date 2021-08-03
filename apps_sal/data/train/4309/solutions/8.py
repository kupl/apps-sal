from collections import Counter
from itertools import chain, groupby, repeat, starmap

C2D = {'!': 1, '?': -1}


def replace(s):
    gs = [(c, sum(1 for _ in g)) for c, g in groupby(s)]
    ds = Counter()
    for c, k in gs:
        ds[k] += C2D[c]
    for i in reversed(list(range(len(gs)))):
        c, k = gs[i]
        if ds[k] * C2D[c] > 0:
            ds[k] -= C2D[c]
        else:
            gs[i] = ' ', k
    return ''.join(chain.from_iterable(starmap(repeat, gs)))
