def bar_triang(pointA, pointB, pointC): # points A, B and C will never be aligned
    xa =  pointA[0]
    xb =  pointB[0]
    xc =  pointC[0]
    ya =  pointA[1]
    yb =  pointB[1]
    yc =  pointC[1]
    xO =  round((xa+xb+xc)/3,4)
    yO =  round((ya+yb+yc)/3,4)
    return [xO, yO] # coordinates of the barycenter expressed up to four decimals
                    # (rounded result)

