def number(bus_stops):
    retval = 0
    for x in bus_stops:
        retval = retval + x[0]
        retval = retval - x[1]
        print(x[1])
    return retval
