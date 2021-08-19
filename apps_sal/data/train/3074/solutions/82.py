def growing_plant(upSpeed, downSpeed, desiredHeight):
    initial = upSpeed
    count = 1
    while initial < desiredHeight:
        initial += upSpeed
        initial -= downSpeed
        count += 1
    return count
    # your code here
