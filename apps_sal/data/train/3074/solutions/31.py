def growing_plant(upSpeed, downSpeed, desiredHeight):
    if upSpeed >= desiredHeight:
        return 1
    days = 0
    plant = 0
    while desiredHeight > plant:
        if plant + upSpeed >= desiredHeight:
            days += 1
            break
        else:
            plant += upSpeed - downSpeed
            days += 1
    return days
