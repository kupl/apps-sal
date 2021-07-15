def bumps(road):
    bumps = 0
    for letter in road:
        if letter == 'n':
            bumps += 1
            continue
        else:
            continue
    if bumps > 15:
        return 'Car Dead'
    else:
        return 'Woohoo!'
