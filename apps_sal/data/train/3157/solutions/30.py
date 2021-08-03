def number(bus_stops):
    on, off = list(map(sum, list(zip(*bus_stops))))
    return on - off
