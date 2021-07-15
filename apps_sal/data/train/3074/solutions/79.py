def growing_plant(upSpeed, downSpeed, desiredHeight):
    t = 0
    day = 0
    while t < desiredHeight:
        day += 1
        t += upSpeed
        if t >= desiredHeight:
            return day
        t -= downSpeed
    return max(day, 1)
