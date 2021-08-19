from itertools import groupby


def happy_g(s):
    return all((False if k == 'g' and len(list(g)) == 1 else True for (k, g) in groupby(s)))
