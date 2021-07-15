def get_real_floor(n):
    if n < 1:
        return n
    elif 1<=n<=12:
        return n-1
    elif n >= 13:
        return n-2
