def segment_cover(points, length):
    (n, e) = (0, float('-inf'))
    for p in sorted(points):
        if e < p:
            e = p + length
            n += 1
    return n
