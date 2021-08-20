def riders(stations, station_x):
    stations.insert(station_x - 2, stations[station_x - 2])
    riders = 1
    miles = 0
    for (i, m) in enumerate(stations):
        miles += m
        if miles > 100:
            miles = m
            riders += 1
        if i == station_x - 2:
            miles = m
            riders += 1
    return riders
