def number(bus_stops):
    res = 0
    for e in bus_stops:
        res += e[0]
        res -= e[1]
    return res
