def number(bus_stops):
    x = 0
    y = 0
    for i in bus_stops:
        x += i[0]
        y += i[1]
    return x - y
