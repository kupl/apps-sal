def number(bus_stops):
    totalnum1 =0
    totalnum2 =0
    for i in range (0,len(bus_stops)):
        totalnum1 = totalnum1 + (bus_stops[i])[0]
        totalnum2 = totalnum2 + (bus_stops[i])[1]
        num = totalnum1 - totalnum2
    return num
