from math import *


def evaporator(content, evap_per_day, threshold):
    return ceil(log(threshold / 100, 1 - evap_per_day / 100))
