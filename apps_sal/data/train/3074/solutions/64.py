def growing_plant(upSpeed, downSpeed, desiredHeight):
    (height, day) = (upSpeed, 1)
    while height < desiredHeight:
        print('After day ' + str(day) + ' --> ' + str(height))
        print('After night ' + str(day) + ' --> ' + str(height - downSpeed))
        height = height - downSpeed + upSpeed
        day += 1
    print('After day ' + str(day) + ' --> ' + str(height))
    return day
