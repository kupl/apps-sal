def past(h, m, s):
    ms = 0
    ms += 3600000 * h
    ms += 60000 * m
    ms += 1000 * s
    return ms
