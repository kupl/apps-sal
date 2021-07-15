def number(bus_stops):
    ppl = 0
    for stops in bus_stops:
        ppl += stops[0]
        ppl -= stops[1]
    return ppl
