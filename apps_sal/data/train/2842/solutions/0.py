def coordinates(p1,p2, precision = 0):
    return round(sum( (b-a)**2 for a,b in zip(p1,p2) )**.5, precision)
