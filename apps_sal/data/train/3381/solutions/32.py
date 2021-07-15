def get_real_floor(n):
    if n>13:
        f = n-2
    elif n>1 and n<13:
        f = n-1
    elif n<0:
        f = n
    else: f = 0
    return f
