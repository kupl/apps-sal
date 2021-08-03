from math import ceil


def snail(column, day, night):
    return ceil((column - night) / (day - night)) if column - day > 0 else 1
