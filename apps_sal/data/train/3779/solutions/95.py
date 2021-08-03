def past(h, m, s):
    if h:
        m += h * 60
    if m:
        s += m * 60
    return s * 1000
