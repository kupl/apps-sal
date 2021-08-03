import math


def calculate_scrap(scraps, num):
    mat = num * 50
    for x in scraps:
        mat = mat / (0.01 * (100 - x))
    return math.ceil(mat)
