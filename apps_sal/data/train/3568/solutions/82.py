def bumps(road):
    bumps = 0
    for i in range(len(road)):
        if road[i] == "n":
            bumps = bumps + 1

    if bumps > 15:
        return "Car Dead"
    else:
        return "Woohoo!"
