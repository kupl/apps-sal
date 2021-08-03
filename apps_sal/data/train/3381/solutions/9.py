def get_real_floor(n):
    if 1 <= n < 13:
        return n - 1
    if 13 <= n:
        return n - 2
    if n <= 0:
        return n
