def growing_plant(upSpeed, downSpeed, desiredHeight):
    progress = upSpeed - downSpeed
    total = 1
    while upSpeed < desiredHeight:
        upSpeed += progress
        total += 1
    return total
