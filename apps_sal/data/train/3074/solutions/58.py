def growing_plant(upSpeed, downSpeed, desiredHeight):
    if desiredHeight <= downSpeed:
        return 1
    currentHeight = 0
    i = 1
    while i < 100000:
        currentHeight += upSpeed
        if currentHeight >= desiredHeight:
            break
        currentHeight -= downSpeed
        i += 1
    return i
