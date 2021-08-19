def bus_timer(time):
    print(time)
    (hour, mins) = map(int, time.split(':'))
    mins += hour * 60
    if 0 <= mins < 355 or mins > 1435:
        return 355 - mins + 1440 * (mins > 1435)
    mins = 10 - mins + mins // 15 * 15
    return mins + 15 * (mins < 0)
