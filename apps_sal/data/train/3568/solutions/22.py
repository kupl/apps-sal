def bumps(road):
    bumps = road.count("n")
    if bumps > 15:
        return "Car Dead"
    elif bumps <= 15:
        return "Woohoo!"
