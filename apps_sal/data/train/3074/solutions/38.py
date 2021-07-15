def growing_plant(upSpeed, downSpeed, desiredHeight):
    height = days = 0
    while height <= desiredHeight:
        days += 1
        height += upSpeed
        if height >= desiredHeight: break
        height -= downSpeed
    return days
