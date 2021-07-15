def number(bus_stops):
    sum_in_bus = 0
    
    for stop in bus_stops:
        sum_in_bus += stop[0] - stop[1]
        
    return sum_in_bus
