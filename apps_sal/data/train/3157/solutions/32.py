def number(bus_stops):
    x = 0
    for (go, out) in bus_stops:
        x += go - out
    return x
