def past(h, m, s):
    if h == 0:
        pass
    else:
        h = 3600000 * h
    if m == 0:
        pass
    else:
        m = 60000 * m
    if s == 0:
        pass
    else:
        s = 1000 * s
    return (h + m + s)
