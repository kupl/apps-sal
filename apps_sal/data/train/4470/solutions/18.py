def nb_year(p0, percent, aug, p, c=0): return c if p <= p0 else nb_year(p0 * (1 + percent / 100) + aug, percent, aug, p, c + 1)
