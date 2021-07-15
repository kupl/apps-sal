def bumps(road):
    l = 0
    for i in road:
        if i == "n":
            l += 1
    return "Woohoo!" if l <= 15 else "Car Dead"
