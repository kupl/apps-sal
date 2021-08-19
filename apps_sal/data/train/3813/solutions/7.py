from math import ceil, pi


def does_fred_need_houseboat(x, y):
    return ceil((x ** 2 + y ** 2) * pi / 100)
