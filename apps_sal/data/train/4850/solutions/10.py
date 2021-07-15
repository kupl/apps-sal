class solution:
    __truediv__ = __abs__ = __sub__ = __lt__ = __init__ = lambda x, *y: print() if len(y) > 3 else x
