def growing_plant(upSpeed, downSpeed, desiredHeight):
    (h, day) = (0, 1)
    while h != desiredHeight:
        h += upSpeed
        if h >= desiredHeight:
            break
        h -= downSpeed
        day += 1
    return day
