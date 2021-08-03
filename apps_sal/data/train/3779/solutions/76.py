def past(h, m, s):
    ms = 0
    if h >= 0 and h <= 23:
        ms += h * 3600000
    else:
        ms += 0

    if m >= 0 and m <= 59:
        ms += m * 60000
    else:
        ms += 0

    if s >= 0 and s <= 59:
        ms += s * 1000
    else:
        ms += 0

    return ms
