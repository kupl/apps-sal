def array_equalization(a, k):
    n, r = len(a), len(a)
    for x in set(a):
        i, t = 0, 0
        while i < n:
            if a[i] != x:
                t += 1
                i += k
            else:
                i += 1
        r = min(r, t)
    return r
