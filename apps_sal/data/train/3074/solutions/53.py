def growing_plant(upSpeed, downSpeed, desiredHeight):
    days = 0
    h = 0
    while True:
        days = days + 1
        h = h + upSpeed
        if h >= desiredHeight:
            return days
        else:
            h = h - downSpeed
