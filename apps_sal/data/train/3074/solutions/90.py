def growing_plant(upSpeed, downSpeed, desiredHeight):
    h = 0
    counter = 1
    while h + upSpeed < desiredHeight:
        h += upSpeed - downSpeed
        counter += 1
    return counter
