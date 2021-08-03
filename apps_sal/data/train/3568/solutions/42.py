def bumps(road):
    n = 0
    for char in road:
        if char == "n":
            n += 1
    if n > 15:
        return "Car Dead"
    else:
        return "Woohoo!"
