def growing_plant(upSpeed, downSpeed, desiredHeight):
    try:
        assert 5 <= upSpeed <= 100
        assert 2 <= downSpeed < upSpeed
        assert 4 <= desiredHeight <= 1000
    except:
        return 1
    day = 0
    plantHeight = 0
    while plantHeight < desiredHeight:
        day += 1
        plantHeight += upSpeed
        if plantHeight >= desiredHeight:
            break
        else:
            plantHeight -= downSpeed
    return day
