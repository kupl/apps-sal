def growing_plant(upSpeed, downSpeed, desiredHeight):
    t = 0
    h = 0
    while True:
        t += 1
        h += upSpeed
        if h >= desiredHeight:
            return t
        h -= downSpeed
