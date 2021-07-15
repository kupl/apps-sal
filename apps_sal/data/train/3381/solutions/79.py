def get_real_floor(n):
    if n <= 0:
        return n
    if 0 < n < 13:
        return n-1
    if 13 < n:
        return n-2
