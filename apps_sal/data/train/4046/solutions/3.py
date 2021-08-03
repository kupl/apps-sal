def calculate_scrap(scraps, number_of_robots):

    iron = 50 * number_of_robots

    for x in range(len(scraps)):
        iron = iron / (1 - scraps[x] / 100)
    return round(iron + 0.5)
