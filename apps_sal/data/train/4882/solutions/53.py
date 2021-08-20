def round_to_next5(n):
    i = 0
    if n == 0:
        return 0
    for i in range(20000):
        if 5 * (i + 1) >= n > 0:
            return 5 * (i + 1)
            break
        elif -5 * (i + 1) < n < 0:
            return -5 * i
