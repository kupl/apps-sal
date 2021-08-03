def number(bus_stops):
    empty = []
    for i in range(0, len(bus_stops)):
        empty.append(bus_stops[i][0] - bus_stops[i][1])
    return sum(empty)
