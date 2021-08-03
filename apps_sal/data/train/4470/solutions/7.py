def nb_year(p0, percent, aug, p):
    y = 0
    while p0 < p:
        p0, y = p0 * (1 + percent / 100.0) + aug, y + 1
    return y
