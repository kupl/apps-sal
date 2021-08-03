def nb_year(p0, percent, aug, p):
    current_population = p0
    years = 0
    while current_population < p:
        new_population = current_population + current_population * percent / 100 + aug
        current_population = new_population
        years += 1
    return years
