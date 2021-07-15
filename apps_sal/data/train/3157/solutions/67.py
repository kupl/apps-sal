def number(bus_stops):
    on_sum = 0
    off_sum = 0
    for x in bus_stops:
        on_sum += x[0]
        off_sum += x[1]
    return on_sum - off_sum    
    # Good Luck!

