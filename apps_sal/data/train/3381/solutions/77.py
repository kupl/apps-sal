def get_real_floor(n):
    if n < 0:
        return n
    if n > 13:
        return n - 2
    else:
        return max(0, n - 1)
