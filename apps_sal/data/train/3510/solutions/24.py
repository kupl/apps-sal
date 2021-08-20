import math


def count_red_beads(n):
    if n < 2:
        return 0
    else:
        if n % 2 != 0:
            g = math.floor(n / 2)
            d = g * 4
            return d
        if n % 2 == 0:
            g = math.floor(n / 2)
            d = g * 4
            return d - 2
