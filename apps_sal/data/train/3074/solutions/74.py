def growing_plant(upSpeed, downSpeed, desiredHeight):
    height = 0
    days = 0
    heights = []
    if desiredHeight == 0:
        return 1
    while height < desiredHeight:
        height += upSpeed
        days += 1
        if height >= desiredHeight:
            break
        height -= downSpeed
    return days
