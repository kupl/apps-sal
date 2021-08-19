def time(distance, boat_speed, stream):
    stream_speed = int(stream.split()[1])
    if stream[0] == 'D':
        speed = boat_speed + stream_speed
    else:
        speed = boat_speed - stream_speed
    return round(distance / speed, 2)
