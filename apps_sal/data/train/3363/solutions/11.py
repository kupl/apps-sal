from math import log2, ceil


def evaporator(content, evap_per_day, threshold):
    return ceil(log2(threshold / 100.0) / log2(1 - evap_per_day / 100.0))
