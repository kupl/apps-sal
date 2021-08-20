def riders(stations):
    count = 1
    distance = 0
    for station in stations:
        if distance + station > 100:
            count += 1
            distance = 0
        distance += station
    return count
