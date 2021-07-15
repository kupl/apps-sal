def bumps(road):
    fiut=0
    for n in road:
        if n == "n":
            fiut += 1
    if fiut>15:
        return "Car Dead"
    else:
        return "Woohoo!"
