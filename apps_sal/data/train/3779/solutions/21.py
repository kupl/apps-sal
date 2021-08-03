def past(h, m, s):
    if h != 0:
        h = h * 3600000
    if m != 0:
        m = m * 60000
    if s != 0:
        s = s * 1000

    return s + m + h
