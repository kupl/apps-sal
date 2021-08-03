def paperwork(n, m):
    if n < 0 and m < 0:
        return 0
    return max(n * m, 0)
