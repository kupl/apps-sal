def past(h, m, s):
    x = 0
    if h:
        x += h * 3600000
    if m:
        x += m * 60000
    if s:
        x += s * 1000
    return x
