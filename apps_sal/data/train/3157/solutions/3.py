def number(bus_stops):
    sum=0
    for i in bus_stops:
        sum+=i[0]-i[1]
    return sum
