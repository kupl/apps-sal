def getSlope(p1, p2):
    (p1x, p1y) = p1
    (p2x, p2y) = p2
    try:
        return (p2y - p1y) / (p2x - p1x)
    except:
        pass
