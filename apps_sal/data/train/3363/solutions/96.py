import numpy as np


def evaporator(content, evap_per_day, threshold):
    return np.ceil(np.log(threshold / 100) / np.log(1 - evap_per_day / 100))
