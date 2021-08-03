import math


def starting_mark(h):
    x = (10.67 - 9.45) / (1.83 - 1.52)
    return round((x * h + 10.67 - x * 1.83), 2)
