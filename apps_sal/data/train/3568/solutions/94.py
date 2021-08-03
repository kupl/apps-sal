def bumps(road):
    b = 0
    for x in road:
        if x == 'n':
            b = b + 1
    if b < 15:
        return "Woohoo!"
    elif b == 15:
        return "Woohoo!"
    else:
        return "Car Dead"
