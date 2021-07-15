def bumps(road):
    count = 0
    for each in road:
        if each == "n":
            count += 1
    if count > 15:
        return "Car Dead"
    elif count <= 15:
        return "Woohoo!"
