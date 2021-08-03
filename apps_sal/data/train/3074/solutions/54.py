def growing_plant(upSpeed, downSpeed, desiredHeight):
    height = upSpeed
    day = 1

    while(height < desiredHeight):
        height -= downSpeed
        height += upSpeed
        day += 1

    return day
