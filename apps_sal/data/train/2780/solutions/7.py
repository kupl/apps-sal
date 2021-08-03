def time(distance, boat_speed, stream):

    s = stream.split()

    net_speed = boat_speed + int(s[1]) if s[0] == 'Downstream' else boat_speed - int(s[1])

    return round(distance / net_speed, 2)
