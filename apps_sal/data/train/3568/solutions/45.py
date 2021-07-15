def bumps(road):
    count = 0
    for x in road:
        if x is "n":
            count = count + 1
    if count > 15: x = "Car Dead"
    else: x = "Woohoo!"
    return x
