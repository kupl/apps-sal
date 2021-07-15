def number(bus_stops):
    present = 0
    for tup in bus_stops:
        present = present + tup[0]
        present = present - tup[1]
    return present
        

