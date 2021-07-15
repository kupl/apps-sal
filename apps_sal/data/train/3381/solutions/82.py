def get_real_floor(n):
    if n < 14 and n >= 1:
        return n-1
    if n >= 14:
        return n-2
    if n == -1:
        return n+1  
    else:
        return n
