def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 += ((p0 / 100) * percent) + aug
        years += 1
    return years


print(nb_year(1500000, 0.25, 1000, 2000000))
