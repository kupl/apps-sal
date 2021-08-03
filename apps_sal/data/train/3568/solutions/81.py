def bumps(road):
    num = 0
    for x in road:
        if x == 'n':
            num += 1
    if num <= 15:
        return 'Woohoo!'
    else:
        return 'Car Dead'
