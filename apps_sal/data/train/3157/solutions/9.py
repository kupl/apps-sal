def number(bus_stops):
    return sum([item[0] - item[1] for item in bus_stops])
