def getSlope(p1, p2):
    if not (p2[0] - p1[0]):
        return None
    return (p2[1] - p1[1]) / (p2[0] - p1[0])
