def growing_plant(upSpeed, downSpeed, desiredHeight):
    plantHeight = 0
    day = 0
    night = 0

    while plantHeight != desiredHeight:
        day += 1
        plantHeight += upSpeed
        if plantHeight >= desiredHeight:
            return day

        night += 1
        plantHeight -= downSpeed
        if plantHeight >= desiredHeight:
            return night
