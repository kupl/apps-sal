def number(bus_stops):
    getin = 0
    getout = 0
    for (x, y) in bus_stops:
        getin += x
        getout += y
    return getin - getout
