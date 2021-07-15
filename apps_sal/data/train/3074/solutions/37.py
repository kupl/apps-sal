def growing_plant(up, down, desired):
    res, day = 0, 0
    while True:
        res += up
        day += 1
        if res >= desired:
            return day
        res -= down
