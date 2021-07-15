def bar_triang(pointA, pointB, pointC): # points A, B and C will never be aligned
    # your code here
    x0=pointA[0]+pointB[0]+pointC[0]
    y0=pointA[1]+pointB[1]+pointC[1]
    x0=round(x0/3,4)
    y0=round(y0/3,4)
    return [x0, y0] # coordinates of the barycenter expressed up to four decimals
                    # (rounded result)

