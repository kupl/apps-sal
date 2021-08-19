def riders(stations, station_x):
    riders = 1
    index = 1
    r_miles = 0

    for s_distance in stations:
        index += 1
        r_miles += s_distance

        if r_miles > 100:
            riders += 1
            r_miles = s_distance

        if station_x == index:
            riders += 1
            r_miles = (s_distance * 2)
            if r_miles > 100:
                riders += 1
                r_miles = s_distance
    return riders

    #print (stations)
    #print (station_x)
