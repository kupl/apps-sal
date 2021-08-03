def bar_triang(a, b, c):  # points A, B and C will never be aligned
    xO = (a[0] + b[0] + c[0]) / 3
    yO = (a[1] + b[1] + c[1]) / 3
    return [round(xO, 4), round(yO, 4)]  # coordinates of the barycenter expressed up to four decimals
    # (rounded result)
