def riders(stations):
    (riders, distance) = (1, 0)
    for i in stations:
        distance += i
        if distance > 100:
            (riders, distance) = (riders + 1, i)
    return riders
