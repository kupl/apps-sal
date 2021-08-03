def number(bus_stops):
    # Good Luck!
    left_on_bus = 0
    for i in bus_stops:
        left_on_bus += (i[0]) - (i[1])
    return left_on_bus
