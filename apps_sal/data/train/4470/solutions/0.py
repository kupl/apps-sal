def nb_year(population, percent, aug, target):
    year = 0
    while population < target:
        population += population * percent / 100.0 + aug
        year += 1
    return year
