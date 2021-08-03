from numpy import ceil


def snail(column, day, night):
    return max(ceil((column - day) / (day - night)), 0) + 1
