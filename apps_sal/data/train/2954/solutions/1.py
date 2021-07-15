def riders(stations):
    n = 1
    acc = 0
    for x in stations:
        acc += x
        if acc > 100:
            acc = x
            n += 1
    return n
