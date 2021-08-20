from math import ceil


def calculate_scrap(scraps, number_of_robots):
    if len(scraps) == 1:
        return ceil(50 * number_of_robots / ((100 - scraps[0]) / 100))
    else:
        divisor = 1
        for i in scraps:
            divisor *= (100 - i) / 100
        return ceil(50 * number_of_robots / divisor)
