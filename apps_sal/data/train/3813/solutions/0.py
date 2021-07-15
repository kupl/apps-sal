from math import ceil, pi

def does_fred_need_houseboat(x, y):
    return ceil(pi * (x**2 + y**2) / 100)
