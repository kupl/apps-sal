import math


def evaporator(content, evap_per_day, threshold):
    (evap_per_day, threshold) = (evap_per_day / 100.0, threshold / 100.0)
    return math.ceil(math.log(threshold) / math.log(1 - evap_per_day))
