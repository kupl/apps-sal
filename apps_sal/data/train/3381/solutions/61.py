def get_real_floor(n):
    if n == 1:
        return 0
    if n > 13:
        return n - 2
    if n < 0:
        return n
    if n > 0 and n < 13:
        return n - 1
    return 0
