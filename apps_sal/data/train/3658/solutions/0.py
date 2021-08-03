from itertools import cycle


def swap(s, n):
    b = cycle(bin(n)[2:])
    return "".join(c.swapcase() if c.isalpha() and next(b) == '1' else c for c in s)
