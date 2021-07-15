def nb_year(p0, percent, ag, p):
    year = 0
    while p0 < p:
        year += 1
        p0 = p0 * (1+percent/100) + ag
    return year
