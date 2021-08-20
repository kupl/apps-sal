def growing_plant(upSpeed, downSpeed, desiredHeight):
    (h, c) = (upSpeed, 0)
    while h < desiredHeight:
        h = h - downSpeed + upSpeed
        c = c + 1
    return c + 1
