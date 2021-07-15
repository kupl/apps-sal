def growing_plant(upSpeed, downSpeed, desiredHeight):
    day = 0
    height = 0
    while desiredHeight > height:
        day += 1
        height += upSpeed
        if height >= desiredHeight:
            return day
        height -= downSpeed
    return day if day > 0 else 1   
