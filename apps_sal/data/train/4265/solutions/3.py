def tops(stg):
    l = int((1 + (1 + 8 * len(stg)) ** 0.5) / 4)
    return ''.join((stg[n * (2 * n - 1)] for n in range(l, 0, -1)))
