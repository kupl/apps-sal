def get_real_floor(n):
    if n == 0:
        return 0
    if 0 < n <= 13:
        return n-1
    
    return n-2 if n > 13 else n
