def growing_plant(upSpeed, downSpeed, desiredHeight):
    i = 0
    total = 0
    up = 0
    if desiredHeight == 0:
        return 1
    while total < desiredHeight and up < desiredHeight:
        i += 1
        up = total + upSpeed
        total = total + upSpeed - downSpeed
    return i
