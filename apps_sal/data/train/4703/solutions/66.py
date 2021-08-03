def bar_triang(pointA, pointB, pointC):
    # points A, B and C will never be aligned
    # coordinates of the barycenter expressed up to four decimals
    # (rounded result)
    return [round((pointA[i] + pointB[i] + pointC[i]) / 3, 4) for i in range(2)]
