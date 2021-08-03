def number(bus_stops):

    bus_pop = 0

    for stop in bus_stops:
        bus_pop += stop[0]
        bus_pop -= stop[1]

    return bus_pop
