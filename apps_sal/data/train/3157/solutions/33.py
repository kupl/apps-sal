def number(bus_stops):
    still_in_bus = 0
    for stop in bus_stops:
        still_in_bus = still_in_bus + (stop[0] - stop[1])
    return still_in_bus
