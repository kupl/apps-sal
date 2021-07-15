def growing_plant(upSpeed, downSpeed, desiredHeight):
    count = 0
    while desiredHeight >= 0:
        count += 1
        desiredHeight -= upSpeed
        if desiredHeight <= 0:
            break
        desiredHeight += downSpeed
    return count
