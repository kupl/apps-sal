def growing_plant(upSpeed, downSpeed, desiredHeight):
    height = 0
    day = 1
    while height < desiredHeight:
        if height + upSpeed >= desiredHeight:
            return day
        else:
            height += upSpeed - downSpeed
            day += 1
    return day
