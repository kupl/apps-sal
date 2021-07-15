def number(bus_stops):
#     a = sum([i[0] for i in bus_stops])
#     b = sum([i[1] for i in bus_stops])
#     return a-b
    return sum([i[0] for i in bus_stops])-sum([i[1] for i in bus_stops])
