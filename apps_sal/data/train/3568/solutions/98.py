def bumps(road):
    badNumber = 15
    count = 0
    for i in range(len(road)):
        if road[i] == "n":
            count += 1
    if count <= badNumber:
        return "Woohoo!"
    if count > badNumber:
        return "Car Dead"
