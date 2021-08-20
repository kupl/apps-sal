def harmon_pointTrip(a, b, c):
    return round(((c - a) * b + (c - b) * a) / (1.0 * (c - b) + (c - a)), 4)
