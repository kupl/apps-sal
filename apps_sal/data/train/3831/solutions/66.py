def angle(n):
    if n == 3:
        return 180
    else:
        return angle(n - 1) + 180
