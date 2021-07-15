def bumps(road):
    # your code here
    bumps = 0
    for i in road:
        if i == '_':
            pass
        elif i == 'n':
            bumps += 1
    if bumps > 15:
        return "Car Dead"
    else:
        return "Woohoo!"
