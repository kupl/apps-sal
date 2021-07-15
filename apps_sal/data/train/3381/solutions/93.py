def get_real_floor(n):
    if n < 0:
        return n
    return max(0, n - 1) if n < 13 else n - 2
