def number(bus_stops):

    came = 0
    left = 0
    for counter, _ in enumerate(bus_stops, 0):
        came = came + bus_stops[counter][0]
        left = left + bus_stops[counter][1]
    return came - left
