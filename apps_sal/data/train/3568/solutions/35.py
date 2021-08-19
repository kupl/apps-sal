def bumps(road):
    x = 0
    for i in road:
        if i == 'n':
            x += 1
    if x > 15:
        return 'Car Dead'
    else:
        return 'Woohoo!'
