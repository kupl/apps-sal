def growing_plant(upSpeed, downSpeed, desiredHeight):
    growth = upSpeed
    count = 1
    while growth < desiredHeight:
        growth -= downSpeed
        count += 1
        growth += upSpeed
    return count
