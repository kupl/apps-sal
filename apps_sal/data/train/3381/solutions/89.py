def get_real_floor(n):
    if n<=0:
        return n
    elif n<=1 or n<=12:
        return n-1
    else:
        return n-2
