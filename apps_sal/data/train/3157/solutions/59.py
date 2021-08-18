def number(bus_stops):
    return sum([i[0] for i in bus_stops]) - sum([i[1] for i in bus_stops])
