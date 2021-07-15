def growing_plant(upSpeed, downSpeed, desiredHeight):
    growth = 0
    count = 1
    while growth < desiredHeight:
        growth += upSpeed
        if growth >= desiredHeight:
            return count
        count += 1
        growth -= downSpeed
    return count
