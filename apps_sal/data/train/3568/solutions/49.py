def bumps(road):
    x = 0
    for spot in road:
        if spot == 'n':
            x += 1
        else:
            continue
    if x > 15:
        return "Car Dead"
    else:
        return "Woohoo!"
