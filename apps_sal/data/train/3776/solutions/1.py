def segment_cover(a, l):
    a, n = set(a), 0
    while a:
        a -= set(range(min(a), min(a) + l + 1))
        n += 1
    return n
