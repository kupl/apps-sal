def number(bus_stops):
    b = 0
    for enter, leave in bus_stops:
        b = max(b + enter - leave, 0)
    return b

