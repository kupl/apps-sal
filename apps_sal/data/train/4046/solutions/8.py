from math import ceil

def calculate_scrap(scraps, number_of_robots):
    factor = 1
    for x in scraps:
        factor *= 1 - x / 100
    return ceil(50 / factor * number_of_robots)
