from itertools import starmap
from operator import sub


def number(bus_stops):
    return sum(starmap(sub, bus_stops))
