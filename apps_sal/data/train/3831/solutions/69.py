def angle(n):
    if n <= 2:
        raise ValueError
    else:
        return 180 * (int(n) - 2)
