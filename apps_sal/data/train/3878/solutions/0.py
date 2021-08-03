def kangaroo(k1, r1, k2, r2):
    if r1 == r2:
        return k1 == k2
    cross, r = divmod(k1 - k2, r2 - r1)
    return cross >= 0 and not r
