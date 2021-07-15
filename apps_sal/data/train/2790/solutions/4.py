from itertools import groupby

def dup(strings):
    return [''.join(c for c, _ in groupby(s)) for s in strings]
