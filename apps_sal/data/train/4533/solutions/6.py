def harmon_pointTrip(xA, xB, xC):
    return round((xA * xC + xB * xC - 2 * xA * xB) / float(2 * xC - xA - xB), 4)
