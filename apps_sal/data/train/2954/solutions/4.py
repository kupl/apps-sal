def riders(stations):
    res = 0
    rdistance = 0
    for i in stations:
        if rdistance + i > 100:
            rdistance = i
            res += 1
        else:
            rdistance += i
    return res + 1
