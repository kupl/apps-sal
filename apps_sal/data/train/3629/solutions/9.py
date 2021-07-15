def array_mash(a, b):
    r = [None] * (len(a) + len(b))
    r[::2] = a
    r[1::2] = b
    return r
