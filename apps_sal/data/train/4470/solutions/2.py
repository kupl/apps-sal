def nb_year(p0, percent, aug, p):
    return 0 if p0 >= p else nb_year(p0 + p0 * percent/100 + aug, percent, aug, p)+1

