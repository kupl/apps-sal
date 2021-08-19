def number(bus_stops):
    # bus_stops[0][0]
    # bus_stops[1][0]
    # bus_stops[2][0]

    # bus_stops[0][1]
    # bus_stops[1][1]
    # bus_stops[2][1]
    came = 0
    left = 0
    for counter, _ in enumerate(bus_stops, 0):
        came = came + bus_stops[counter][0]
        left = left + bus_stops[counter][1]
    return came - left
