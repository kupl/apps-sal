def time(distance, boat_speed, stream):
    (direction, speed_str) = stream.split()
    speed = int(speed_str) * (1 if direction == 'Downstream' else -1)
    return round(distance / (boat_speed + speed), 2)
