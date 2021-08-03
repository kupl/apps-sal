def growing_plant(upSpeed, downSpeed, desiredHeight):
    count = 1
    height = 0
    while height < desiredHeight:
        height = height + upSpeed
        if height >= desiredHeight:
            break
        height = height - downSpeed
        if height >= desiredHeight:
            break
        count = count + 1
    return count
