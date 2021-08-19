def bumps(road):
    bumps = 0
    for char in road:
        if char == 'n':
            bumps = bumps + 1
    if bumps <= 15:
        return 'Woohoo!'
    else:
        return 'Car Dead'
