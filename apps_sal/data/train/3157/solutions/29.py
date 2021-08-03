import operator


def number(bus_stops):
    return operator.sub(*map(sum, zip(*bus_stops)))
