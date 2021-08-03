def bus_timer(current_time):
    h, m = map(int, current_time.split(':'))

    if h < 6:
        m = (5 - h) * 60 + 60 - m
    elif h == 23 and m > 55:
        return 355 + 60 - m
    else:
        m = 15 - m % 15

    if m > 4:
        return m - 5
    else:
        return m + 10
