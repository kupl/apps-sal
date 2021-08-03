def number(bus_stops):
    peoples = 0
    for number in bus_stops:
        peoples += number[0] - number[1]
    return peoples
