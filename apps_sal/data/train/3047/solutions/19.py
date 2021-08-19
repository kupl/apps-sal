from itertools import groupby


def repeating_fractions(n, d):
    (x, y) = str(n / d).split('.')
    return f'{x}.' + ''.join((f'({k})' if len(list(g)) > 1 else k for (k, g) in groupby(y)))
