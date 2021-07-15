def growing_plant(upSpeed, downSpeed, desiredHeight):
    days = 0
    height = 0
    while True:
        days += 1
        height += upSpeed
        if height >= desiredHeight:
            break
        height -= downSpeed
    return days
