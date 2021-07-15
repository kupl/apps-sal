def number(bus_stops):
    return sum(map(lambda x: x[0]-x[1],bus_stops))
