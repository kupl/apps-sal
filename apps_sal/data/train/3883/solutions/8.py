from itertools import zip_longest


def solve(s):
    (a, b) = (sorted((x for x in s if x in 'aiueo')), sorted((x for x in s if x not in 'aiueo')))
    if len(b) > len(a):
        (a, b) = (b, a)
    return 'failed' if len(a) - len(b) > 1 else ''.join((f'{x}{y}' for (x, y) in zip_longest(a, b, fillvalue='')))
