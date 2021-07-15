def bumps(road):
    count = 0
    for c in road:
        if c == 'n':
            if count == 15:
                return "Car Dead"
            count += 1
    return "Woohoo!"
