def number(bus_stops):
    x = 0
    for i, j in bus_stops:
        x += i - j
    return x
