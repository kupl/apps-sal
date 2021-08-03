from math import floor


def nb_year(p0, percent, aug, p):
    i = 1
    mult = 1 + percent / 100.0
    prev = p0
    while (prev < p):
        ne = floor((prev * mult + aug))
        prev = ne
        i += 1
    return (i - 1)
