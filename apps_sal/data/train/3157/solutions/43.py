def number(bus_stops):
    return sum((bus_stops[0] for bus_stops in bus_stops)) - sum((bus_stops[1] for bus_stops in bus_stops))
