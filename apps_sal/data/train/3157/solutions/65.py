def number(bus_stops):
    inBus = 0
    for stop in bus_stops:
        inBus += stop[0]
        inBus -= stop[1]
        if inBus < 0:
            return False
    return inBus
