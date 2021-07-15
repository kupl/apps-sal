def bar_triang(pointA, pointB, pointC): # points A, B and C will never be aligned
    xO, yO = round((pointA[0] + pointB[0] + pointC[0]) / 3, 4), round((pointA[1] + pointB[1] + pointC[1]) / 3, 4)
    return [xO, yO] # coordinates of the barycenter expressed up to four decimals
                    # (rounded result)

