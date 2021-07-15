def riders(stations):
    s = 0
    r = 1
    for a, n in zip(stations, stations[1:]):
        s += a
        if s + n > 100:
            r += 1
            s = 0
    return r
