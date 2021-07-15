def getSlope(p1, p2):
    ''' Return the slope of the line through p1 and p2
    '''
    if p1[0]==p2[0] or p1==p2:
        return None

    return (p1[1]-p2[1])/(p1[0]-p2[0])
