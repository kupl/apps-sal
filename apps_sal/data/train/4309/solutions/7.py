from itertools import groupby


def replace(s):
    g = [''.join(j) for (i, j) in groupby(s)]
    for (i, j) in enumerate(g):
        for (k, l) in enumerate(g[i + 1:], start=i + 1):
            if len(j) == len(l) and j[0] != l[0] and (' ' not in j + l):
                g[i] = g[k] = ' ' * len(j)
                break
    return ''.join(g)
