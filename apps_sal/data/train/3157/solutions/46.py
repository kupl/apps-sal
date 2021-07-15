def number(bus_stops):
    result = 0
    stop = list(bus_stops)
    for x in stop:
        result = result + x[0] - x[1]
    return result
