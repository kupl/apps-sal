def growing_plant(upSpeed, downSpeed, desiredHeight):
    day = 1
    currentHeight = 0
    growing = True
    while growing:
        currentHeight += upSpeed
        print("After Day", day, "Height:", currentHeight)
        if currentHeight >= desiredHeight:
            growing = False
        else:
            currentHeight -= downSpeed
            print("After Night", day, "Height:", currentHeight)
            day += 1           
    return day
