def bumps(road):
    list = [road]
    a = 0
    for x in road:
        if x == 'n':
            a = a + 1
    if a > 15:
        return 'Car Dead'
    return 'Woohoo!'
