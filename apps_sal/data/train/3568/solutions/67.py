def bumps(road):
    roadList = list(road)
    speedBumps = 'n'
    bumpCount = 0
    for i in roadList:
        if i == 'n':
            bumpCount += 1
    if bumpCount > 15:
        return 'Car Dead'
    else:
        return 'Woohoo!'
