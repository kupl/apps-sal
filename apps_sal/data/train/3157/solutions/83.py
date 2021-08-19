def number(bus_stops):
    remaining = 0
    for (inP, outP) in bus_stops:
        remaining = remaining + inP - outP
    return remaining
