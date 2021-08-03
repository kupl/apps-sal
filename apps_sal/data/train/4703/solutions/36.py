def bar_triang(A, B, C):  # points A, B and C will never be aligned
    # your code here
    return [round((A[0] + B[0] + C[0]) / 3, 4), round((A[1] + B[1] + C[1]) / 3, 4)]  # coordinates of the barycenter expressed up to four decimals
    # (rounded result)
