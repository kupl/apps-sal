def growing_plant(upSpeed, downSpeed, desiredHeight):
    day = 0
    height = 0
    while height < desiredHeight:
        day += 1
        if day != 1:
            height -= downSpeed
        height += upSpeed
    return 1 if desiredHeight == 0 else day
