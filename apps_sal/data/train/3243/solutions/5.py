def bus_timer(current_time):
    hh, mm = [int(v) for v in current_time.split(':')]
    time = (hh * 60 + mm + 5) % 1440
    if time == 0:
        return 0
    if time <= 360:
        return 360 - time
    return -time % 15
