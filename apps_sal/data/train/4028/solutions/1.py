LIMIT = 100

def riders(stations, station_x):
    riders = 1
    rode = 0
    for station, distance in enumerate(stations, 2):
        if rode + distance > LIMIT:
            # Too far, switch riders
            riders += 1
            rode = 0
            
        if station == station_x:
            # Rider lost, send a rescue rider back from station_x
            riders += 1
            if distance > LIMIT / 2:
                # Rescuer would would have to ride too far to return, so need another new rider back to station_x
                riders += 1
                rode = distance
            else:
                # Rescuer is back as original station
                rode = 2 * distance
        else:
            # Carry on to next station, still got plenty of juice
            rode += distance

    return riders

