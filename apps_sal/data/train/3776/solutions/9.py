def segment_cover(a, n):
    a.sort()
    (r, c) = (1, a[0])
    for x in a:
        if x - c > n:
            r += 1
            c = x
    return r
