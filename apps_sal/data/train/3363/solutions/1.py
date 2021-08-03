import math


def evaporator(content, evap_per_day, threshold):
    return math.ceil(math.log(threshold / 100.0) / math.log(1.0 - evap_per_day / 100.0))
