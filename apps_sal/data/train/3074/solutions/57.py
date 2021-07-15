def growing_plant(upSpeed, downSpeed, desiredHeight):
    if desiredHeight == 0:
        return 1
    height = 0
    days = 0
    while height < desiredHeight:
        height += upSpeed
        if height < desiredHeight:
            height -= downSpeed
        days += 1
    return days
