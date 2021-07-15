from math import ceil, log
def evaporator(content, evap_per_day, threshold):
    return ceil(log(threshold/100.0, (100-evap_per_day)/100.0))
