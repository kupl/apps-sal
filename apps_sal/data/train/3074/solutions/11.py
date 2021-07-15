def growing_plant(upSpeed, downSpeed, desiredHeight):
    day = 1
    height = 0
    while True:
        height += upSpeed
        if height >= desiredHeight:
            return day
        height -= downSpeed
        day += 1      
