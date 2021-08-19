def segments(m, a):
    vals = set(range(m + 1))
    for (st, en) in a:
        vals -= set(range(st, en + 1))
    return sorted(vals)
