def number(bus_stops):
    x = 0
    for people in bus_stops:
        x += people[0]
        x -= people[1]
    return x
