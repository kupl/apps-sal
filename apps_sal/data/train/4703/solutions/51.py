def bar_triang(pointA, pointB, pointC):  # points A, B and C will never be aligned
    # print(pointA[0])
    x0 = float(f'{(pointA[0] + pointB[0] + pointC[0])/3 : .4f}')
    y0 = float(f'{(pointA[1] + pointB[1] + pointC[1])/3 : .4f}')
    return [x0, y0]  # coordinates of the barycenter expressed up to four decimals
    # (rounded result)
