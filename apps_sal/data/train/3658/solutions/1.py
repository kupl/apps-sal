from itertools import cycle

def swap(s,n):
    doSwap = cycle(map(int,f"{n:b}"))
    return ''.join(c.swapcase() if c.isalpha() and next(doSwap) else c for c in s)
