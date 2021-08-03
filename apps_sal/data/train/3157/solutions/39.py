from functools import reduce


def number(bus_stops):
    return -reduce(
        lambda x, y: y - x,
        reduce(
            lambda a, b: a + b,
            bus_stops
        )
    )
