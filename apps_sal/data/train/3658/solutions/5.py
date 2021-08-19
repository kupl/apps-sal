from itertools import cycle


def swap(s, n):
    it = cycle(bin(n)[2:])
    return ''.join((x.swapcase() if x.isalpha() and next(it) == '1' else x for x in s))
