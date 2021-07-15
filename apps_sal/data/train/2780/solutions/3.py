def time(distance, boat_speed, stream):
    speed = boat_speed + (int(stream[11:]) if stream[0] == 'D' else -int(stream[9:]))
    return round(distance/speed, 2)
