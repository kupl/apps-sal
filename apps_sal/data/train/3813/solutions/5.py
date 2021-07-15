from math import pi, ceil
def does_fred_need_houseboat(x,y):
    return ceil((x*x + y*y) * pi / 100.0)
