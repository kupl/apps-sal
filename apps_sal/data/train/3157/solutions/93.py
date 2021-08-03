def number(bus_stops):
    number = 0
    for i in range(len(bus_stops)):
        number += bus_stops[i][0] - bus_stops[i][1]
    return number
    # Good Luck!
