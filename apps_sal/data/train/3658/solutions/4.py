from itertools import cycle

def swap(s,n):
    bits = cycle(map(int, f'{n:b}'))
    return ''.join(c.swapcase() if (c.isalpha() and next(bits)) else c for c in s)
