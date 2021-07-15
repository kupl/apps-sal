def growing_plant(upSpeed, downSpeed, desiredHeight):
    day = 0
    night = 0
    height = 0
    while height != desiredHeight:
        height = height + upSpeed
        day = day + 1
        if height >= desiredHeight:
            return day
        else:
            height = height - downSpeed
            night = night + 1
            if height == desiredHeight:
                return night
    return 1
