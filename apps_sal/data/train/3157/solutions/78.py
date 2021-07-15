def number(bus_stops):
    sum_up = 0
    sum_down = 0
    for i in bus_stops:
        sum_up = sum_up + i[0]
        sum_down = sum_down + i[1]
    summ = sum_up-sum_down
    return summ
