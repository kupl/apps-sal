def number(bus_stops):
    a = []
    for l in bus_stops:
        c = l[0] - l[1]
        a.append(c)
    return sum(a)
