def riders(stations, station_x):
    r = 1
    d = 0
    for i, e in enumerate(stations, 1):
        d += e
        if i+1 == station_x:
            r += 1
            d = 2*e
            if d > 100:
                d = e
                r += 1
        if i < len(stations):
            temp = d + stations[i]
            if temp > 100:
                r += 1
                d = 0
    return r
