def number(bus_stops):
    total = 0
    for entered, out in bus_stops:
        total += entered - out 
    return total

