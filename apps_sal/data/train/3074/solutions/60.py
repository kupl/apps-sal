def growing_plant(upSpeed, downSpeed, desiredHeight):
    count = 0
    sum = 0
    while sum < desiredHeight:
        sum += upSpeed
        if sum >= desiredHeight:
            return count + 1
        sum -= downSpeed
        count += 1
        print(sum)
    return 1
