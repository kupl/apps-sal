def number(bus_stops):
    into_bus = 0
    get_off_bus = 0
    for stops in bus_stops:
        into_bus += stops[0]
        get_off_bus += stops[1]
    return into_bus - get_off_bus
