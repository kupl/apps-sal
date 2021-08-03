def nb_year(p0, percent, aug, p):
    # base case
    if p0 >= p:
        return 0

    # recursive case
    _p = percent / 100.00
    p0 = p0 + round(p0 * _p) + aug  # growth of population formula
    return 1 + nb_year(p0, percent, aug, p)
