def bus_timer(time):
    (h, m) = map(int, time.split(':'))
    t = (5 + h * 60 + m) % 1440
    return -t % (360 if t < 360 else 15)
