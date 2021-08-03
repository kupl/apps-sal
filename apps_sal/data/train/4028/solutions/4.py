def riders(stations, station_x):
    riders = 2
    miles = 0
    for i in range(len(stations)):
        if i == station_x - 2:

            miles = stations[i]
        miles += stations[i]
        if miles > 100:
            riders += 1
        if i == len(stations) - 1:
            break
        if miles + stations[i + 1] > 100:
            riders += 1
            miles = 0

    return riders
