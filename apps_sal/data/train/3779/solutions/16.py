def past(h, m, s):
    m += h * 60
    s += m * 60
    ms = s * 1000
    return ms
