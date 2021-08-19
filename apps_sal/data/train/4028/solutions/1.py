LIMIT = 100


def riders(stations, station_x):
    riders = 1
    rode = 0
    for (station, distance) in enumerate(stations, 2):
        if rode + distance > LIMIT:
            riders += 1
            rode = 0
        if station == station_x:
            riders += 1
            if distance > LIMIT / 2:
                riders += 1
                rode = distance
            else:
                rode = 2 * distance
        else:
            rode += distance
    return riders
