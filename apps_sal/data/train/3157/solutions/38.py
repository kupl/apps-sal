def number(bus_stops):
    passengers = 0
    for (x, y) in bus_stops:
        passengers = passengers + x - y
    return passengers
