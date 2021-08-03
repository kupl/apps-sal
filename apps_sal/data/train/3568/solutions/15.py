def bumps(road):
    r = list(road)

    if r.count('n') <= 15:
        return "Woohoo!"
    else:
        return "Car Dead"
