def past(h, m, s):
    a = h * 3600000
    a += m * 60000
    a += s * 1000
    return a
