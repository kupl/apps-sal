def growing_plant(upSpeed, downSpeed, desiredHeight):
    h = 0
    n = 1
    h = n * upSpeed - (n - 1) * downSpeed
    while h < desiredHeight:
        n += 1
        h = n * upSpeed - (n - 1) * downSpeed
    return n
