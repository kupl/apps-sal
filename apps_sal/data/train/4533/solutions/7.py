def harmon_pointTrip(xA, xB, xC):
    n = ((-1) * (xB - xC)) / ((xA - xC) * 1.0)
    xD = ((n * xA) - xB) / (n - 1)
    return round(xD, 4)
