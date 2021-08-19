def growing_plant(upSpeed, downSpeed, desiredHeight):
    i = upSpeed
    j = 1
    while i < desiredHeight:
        i += upSpeed - downSpeed
        j = j + 1
    return j
