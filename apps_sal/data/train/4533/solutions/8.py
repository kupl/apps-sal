def harmon_pointTrip(a, b, c):
    return round(1.0 * (b * (c - a) + a * (c - b)) / (c - a + (c - b)), 4)
