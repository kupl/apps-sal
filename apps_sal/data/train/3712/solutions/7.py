def getSlope(p1, p2):
    ''' Return the slope of the line through p1 and p2
    '''
    try:
        slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
        if (p1 == p2):
            return None
        return slope
    except ZeroDivisionError:
        return None
