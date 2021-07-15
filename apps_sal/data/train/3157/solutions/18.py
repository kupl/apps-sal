def number(bus_stops):
    return sum([bus_in - bus_out for bus_in, bus_out in bus_stops])
