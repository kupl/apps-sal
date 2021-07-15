def number(bus_stops):
    res = [i - j for i, j in bus_stops]
    return sum(res)
