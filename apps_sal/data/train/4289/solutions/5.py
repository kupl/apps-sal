from itertools import groupby


def happy_g(s):
    return all((c != 'g' or sum((1 for _ in g)) > 1 for (c, g) in groupby(s)))
