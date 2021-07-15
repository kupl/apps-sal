def recaman(n):
    k, r, s = 0, 0, 0
    S = {0}
    while n != 0:
        r = k + 1
        if s - r < 0 or s - r in S:
            s += r
        else:
            s -= r
        k += 1
        n -= 1
        S.add(s)
    return s
