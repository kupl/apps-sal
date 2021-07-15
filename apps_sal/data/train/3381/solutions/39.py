def get_real_floor(n):
    if n == 15:
        return 13
    elif n == 0:
        return 0
    elif n >=1 and n < 14:
        return (n-1)
    elif n < 0:
        return n
    else:
        return (n-2)
    # code here

