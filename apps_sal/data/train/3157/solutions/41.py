def number(bus_stops):
    return sum(x[0] for x in bus_stops) - sum(x[1] for x in bus_stops)
