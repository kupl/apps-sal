def bumps(road):
    n = 0
    for i in road:
        if i == 'n':
            n += 1
    if n > 15:
        return "Car Dead"
    return "Woohoo!"    
