def growing_plant(upSpeed, downSpeed, desiredHeight):
    # your code here
    num_days = 1
    height = 0
    while height < desiredHeight:
        height += upSpeed
        if height >= desiredHeight:
            break
        height -= downSpeed
        num_days += 1
    return num_days
