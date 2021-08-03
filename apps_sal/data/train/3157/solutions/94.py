def number(bus_stops):
    up = 0
    down = 0

    for stops in bus_stops:
        up += stops[0]
        down += stops[1]

    return up - down
