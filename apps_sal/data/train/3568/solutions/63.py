def bumps(road):
    bumps = 0
    for a in road:
        if a == 'n':
            bumps += 1
    if bumps <= 15:
        return "Woohoo!"
    else:
        return "Car Dead"
