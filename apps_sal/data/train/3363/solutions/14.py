def evaporator(content, evap_per_day, threshold):
    from math import log, ceil
    return ceil(log(threshold/100) / log(1 - evap_per_day/100))
