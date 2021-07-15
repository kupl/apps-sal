def bumps(road):
    bumps = 0
    for char in road:
        if char == 'n':
            bumps += 1
    if bumps > 15:
        return "Car Dead"
    else:
        return "Woohoo!"
