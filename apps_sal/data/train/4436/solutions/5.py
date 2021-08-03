def S2N(m, n, x=-1, s=0):
    while x < m:
        p = -1
        x += 1
        while p < n:
            p += 1
            s += (x**p)
    return s
