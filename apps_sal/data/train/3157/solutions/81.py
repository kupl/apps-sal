def number(bus_stops):
    res = 0
    for st in bus_stops:
        res = res - st[1]
        res = res + st[0]
    return res
