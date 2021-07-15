def growing_plant(upSpeed, downSpeed, desiredHeight):
    d, h = 0, 0
    while True:
        d += 1
        h += upSpeed
        if h >= desiredHeight:
            return d
        else:
            h -= downSpeed
