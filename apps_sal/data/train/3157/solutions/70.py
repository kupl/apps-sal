def number(bus_stops):
    still_on = 0
    for stop in bus_stops:
        still_on += stop[0]
        still_on -= stop[1]
    return still_on
