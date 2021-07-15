def bumps(road):
    bumps = 0
    for letter in road:
        if letter == 'n' or letter == 'N':
            bumps += 1
        elif letter == '_':
            continue
        else:
            continue
    if bumps > 15:
        return 'Car Dead'
    else:
        return 'Woohoo!'
