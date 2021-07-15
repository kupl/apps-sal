def bumps(road):
    bump = 0
    for x in road:
        if x == "n":
            bump += 1
    if bump <= 15:
        return("Woohoo!")
    else:
        return("Car Dead")
