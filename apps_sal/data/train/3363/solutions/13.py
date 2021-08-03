from math import log


def evaporator(_content, evap_per_day, threshold):
    return int(log(threshold / 100, 1 - evap_per_day / 100) + 1)
