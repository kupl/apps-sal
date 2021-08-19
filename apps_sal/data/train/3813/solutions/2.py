from math import pi, sqrt, hypot
from itertools import count


def radius(year):
    return sqrt(100 * year / pi)


def does_fred_need_houseboat(x, y):
    return next((year for year in count(1) if hypot(x, y) < radius(year)))
