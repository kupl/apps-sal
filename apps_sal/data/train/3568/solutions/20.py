def bumps(road):
    x = road.count("n")
    results = ["Woohoo!", "Car Dead"]

    if x > 15:
        return results[1]
    else:
        return results[0]
