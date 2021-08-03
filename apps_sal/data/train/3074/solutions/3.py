def growing_plant(upSpeed, downSpeed, desiredHeight):
    current = 0
    counter = 1
    while current < desiredHeight:
        current = current + upSpeed
        if current >= desiredHeight:
            return counter
        current = current - downSpeed
        counter = counter + 1
    return counter
