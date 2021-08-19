def get_real_floor(n):
    if n < 0:
        return n
    if n == 0 or n == 1:
        return 0
    elif 2 <= n <= 12:
        return n - 1
    else:
        return n - 2
