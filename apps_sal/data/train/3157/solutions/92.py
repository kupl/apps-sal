def number(bus_stops):
    onBuss = 0

    for i in range(len(bus_stops)):
        onBuss += bus_stops[i][0]
        onBuss -= bus_stops[i][1]
    return onBuss

