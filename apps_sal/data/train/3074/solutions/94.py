def growing_plant(upSpeed, downSpeed, desiredHeight):
    up = upSpeed
    i = 1
    while up < desiredHeight:
        up += upSpeed
        up -= downSpeed
        i += 1
    return i
