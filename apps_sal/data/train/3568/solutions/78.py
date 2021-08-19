def bumps(road):
    dead = 0
    for x in road:
        if x == 'n':
            dead += 1
    if dead > 15:
        return 'Car Dead'
    else:
        return 'Woohoo!'
