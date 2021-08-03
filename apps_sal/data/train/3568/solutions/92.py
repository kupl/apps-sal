def bumps(road):
    count = road.count("n")
    if count > 15:
        return "Car Dead"
    return "Woohoo!"
