def number(bus_stops):
    count = 0
    for el in bus_stops:
        count = count + el[0] - el[1]
    return count
