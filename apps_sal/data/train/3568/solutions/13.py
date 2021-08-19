def bumps(road):
    bumps = 0
    for c in road:
        if c == 'n':
            bumps += 1
    if bumps <= 15:
        return 'Woohoo!'
    else:
        return 'Car Dead'
