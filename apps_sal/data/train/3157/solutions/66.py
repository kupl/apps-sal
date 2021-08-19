def number(bus_stops):
    bus_occupancy = 0
    i = 0
    j = 0
    for i in range(len(bus_stops)):
        bus_occupancy = bus_occupancy + (bus_stops[i][j] - bus_stops[i][j + 1])
        print('Bus occupancy is: ', bus_occupancy)
    return bus_occupancy
