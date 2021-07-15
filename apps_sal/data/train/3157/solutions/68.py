def number(bus_stops):
    x = 0
    for i in bus_stops:
        x = i[0] - i[1] + x
    return x
