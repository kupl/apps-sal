def number(bus_stops):
    counter = 0
    max_index = len(bus_stops) - 1
    y = 0
    z = 0
    while counter <= max_index:
        x = bus_stops[counter]
        counter = counter + 1
        y = y + x[0]
        z = z + x[1]
    end = y - z
    return end
