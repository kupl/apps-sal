import numpy as np


def number(bus_stops):
    bs = np.array(bus_stops)
    return sum(bs[:, 0] - bs[:, 1])
