def past(h, m, s):
    if h:
        return past(0, 60 * h + m, s)
    if m:
        return past(0, 0, 60 * m + s)
    return 1000 * s
