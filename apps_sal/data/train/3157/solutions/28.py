def number(bus_stops):
    return sum([p[0] - p[1] for p in bus_stops])
