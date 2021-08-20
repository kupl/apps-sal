from itertools import zip_longest


def solve(s):
    v = sorted((x for x in s if x in 'aeiou'))
    c = sorted((x for x in s if x not in 'aeiou'))
    if abs(len(v) - len(c)) > 1:
        return 'failed'
    if len(c) > len(v):
        (v, c) = (c, v)
    return ''.join((a + b for (a, b) in zip_longest(v, c, fillvalue='')))
