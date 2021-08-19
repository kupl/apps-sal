from itertools import cycle


def swap(s, n):
    it = cycle(map(int, format(n, 'b')))
    return ''.join((c.swapcase() if c.isalpha() and next(it) else c for c in s))
