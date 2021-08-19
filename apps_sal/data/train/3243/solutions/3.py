def bus_timer(current_time):
    (h, m) = map(int, current_time.split(':'))
    current_time = 60 * h + m
    if current_time >= 1436 or current_time <= 355:
        return (355 - current_time) % 1440
    else:
        return (10 - current_time) % 15
