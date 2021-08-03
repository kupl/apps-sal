def bumps(road):
    bumps = 0
    for ch in road:
        if ch == "n":
            bumps += 1

    if bumps > 15:
        return "Car Dead"
    else:
        return "Woohoo!"
