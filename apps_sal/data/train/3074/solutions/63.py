def growing_plant(upSpeed, downSpeed, desiredHeight):
    height = 0
    day = 0
    if desiredHeight == 0:
        day += 1
        return day
    while height != desiredHeight:
        day += 1
        height += upSpeed
        if height >= desiredHeight:
            return day
        else:
            height -= downSpeed
