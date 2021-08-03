def growing_plant(upSpeed, downSpeed, desiredHeight):
    height = 0
    height2 = 0
    days = 0

    if (desiredHeight == 0):
        return 1

    while height < desiredHeight:
        days += 1
        height = height2
        height += upSpeed
        height2 = height - downSpeed

    return days
