def number(bus_stops):
    get_in, get_off = zip(*bus_stops)
    return sum(get_in) - sum(get_off)
