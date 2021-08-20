from math import hypot, pi, ceil


def does_fred_need_houseboat(x, y):
    return ceil(hypot(x, y) ** 2 * pi / 100)
