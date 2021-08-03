def time(distance, boat_speed, stream):
    direction, stream_speed = tuple(stream.split())
    stream_speed = int(stream_speed)
    if direction == "Downstream":
        if distance % (boat_speed + stream_speed) == 0:
            return int(distance / (boat_speed + stream_speed))
        else:
            return float("%.2f" % (distance / (boat_speed + stream_speed)))
    else:
        if distance % (boat_speed - stream_speed) == 0:
            return int(distance / (boat_speed - stream_speed))
        else:
            return float("%.2f" % (distance / (boat_speed - stream_speed)))
