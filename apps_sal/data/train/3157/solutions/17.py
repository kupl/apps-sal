def number(bus_stops):
    t = 0
    for a in bus_stops:
        t = t + a[0] - a[1]
    return t
