def nb_year(p0, percent, aug, p):
    if p0 >= p:
        return 0
    _p = percent / 100.0
    p0 = p0 + round(p0 * _p) + aug
    return 1 + nb_year(p0, percent, aug, p)
