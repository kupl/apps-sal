from functools import reduce


def number(bus_stops):
    return reduce(lambda i, a: i + a[0] - a[1], bus_stops, 0)
