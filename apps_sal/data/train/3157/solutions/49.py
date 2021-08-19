def number(bus_stops):
    # initialize variables
    x = 0
    # iterate through the arrays and add to the count
    for people in bus_stops:
        x += people[0]
        x -= people[1]
    return x
