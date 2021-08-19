# past = lambda h, m, s: (((60 * h) + m) * 60 + s) * 1000
def past(*ar):
    r = 0
    for x in ar:
        r = 60 * r + x
    return 1000 * r
