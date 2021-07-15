def get_real_floor(n):
    if n == 0: return 0
    elif n > 0: return n - 1 if n <= 13 else n - 2
    else: return n
