def number(bus_stops):
    sleeping = 0
    for i in bus_stops:
        sleeping += i[0] - i[1]
    return sleeping
