def get_real_floor(n):
    if n > 13:
        return n - 2
    elif n > 1 and n < 13:
        return n - 1
    elif n == 1:
        return 0 
    else:
        return n
