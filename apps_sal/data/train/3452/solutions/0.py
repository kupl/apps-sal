from math import ceil


def snail(column, day, night):
    return max(ceil((column-night)/(day-night)), 1)
