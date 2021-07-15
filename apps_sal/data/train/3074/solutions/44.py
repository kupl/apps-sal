def growing_plant(upSpeed, downSpeed, desiredHeight):
    height = 0
    days = 1
    while height < desiredHeight:
        height += upSpeed
        if height < desiredHeight:
            height -= downSpeed
            days += 1
        else:
            return days
