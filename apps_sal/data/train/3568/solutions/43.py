def bumps(road):
    bumps = 0
    for i in range(len(road)):
        if road[i] == "n":
            bumps += 1
        if bumps > 15:
            return "Car Dead"

    return "Woohoo!"
