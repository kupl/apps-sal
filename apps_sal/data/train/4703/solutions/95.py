def bar_triang(pointA, pointB, pointC): # points A, B and C will never be aligned
    # your code here
    xO = round(1/3 * (pointA[0] + pointB[0] + pointC[0]),4)
    yO = round(1/3 * (pointA[1] + pointB[1] + pointC[1]),4)
    return [xO, yO] # coordinates of the barycenter expressed up to four decimals
                    # (rounded result)

