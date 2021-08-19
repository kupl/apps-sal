def harmon_pointTrip(xA, xB, xC):
    a, b, c = list(map(float, [xA, xB, xC]))
    # Yay for algebra!
    d = ((a * c) + (b * c) - (2 * a * b)) / (2 * c - a - b)
    return round(d, 4)
