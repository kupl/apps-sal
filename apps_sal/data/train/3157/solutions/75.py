def number(bus_stops):
    total = 0
    for stop in bus_stops:
        print(stop)
        total = total + stop[0]
        total = total - stop[1]
    
    return total

