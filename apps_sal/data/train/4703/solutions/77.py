def bar_triang(a, b, c):  # points A, B and C will never be aligned
    # your code here
    return [round((a[0] + b[0] + c[0]) / 3, 4), round((a[1] + b[1] + c[1]) / 3, 4)]  # coordinates of the barycenter expressed up to four decimals
    # (rounded result)
