import re


def number_format(n):
    n = str(n)[::-1]
    g = re.split('(\\d{3})', n)
    g = list(filter(None, g))
    if g[-1] == '-':
        return g[-1] + ','.join(g[:-1])[::-1]
    return ','.join(g)[::-1]
