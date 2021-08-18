def number(bus_stops):
    summ = 0
    for i in bus_stops:
        summ += i[0] - i[1]
    return summ
