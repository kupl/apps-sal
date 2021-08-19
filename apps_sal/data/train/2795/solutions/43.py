def cockroach_speed(s):
    temp_speed = 0.036  # 1 sm/sec = 0.036 km/h
    end_speed = s / temp_speed
    return int(end_speed)
