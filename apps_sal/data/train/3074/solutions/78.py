def growing_plant(upSpeed, downSpeed, desiredHeight):
    day = 0
    height = 0

    while height < desiredHeight:
        day += 1
        height += upSpeed
        if height >= desiredHeight:
            return day
        else:
            height -= downSpeed
    return 1
