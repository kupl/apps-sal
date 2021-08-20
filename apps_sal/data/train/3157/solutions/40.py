def number(bus_stops):
    rtn = 0
    for i in bus_stops:
        rtn = rtn + i[0] - i[1]
    return rtn
