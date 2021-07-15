def bar_triang(pointA, pointB, pointC): # points A, B and C will never be aligned
    # your code here
    xO = '{:.4f}'.format(float(pointA[0]+pointB[0]+pointC[0])/3)
    yO = '{:.4f}'.format(float(pointA[1]+pointB[1]+pointC[1])/3)
    return [float(xO), float(yO)] # coordinated of the barycenter expressed up to four decimals
                    # (rounded result)

