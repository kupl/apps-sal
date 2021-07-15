def get_real_floor(n):
    if n>0 and n<13:
        real_floor=n-1
        return real_floor
    if n >=13:
        real_floor=n-2
        return real_floor
    if n<=0:
        real_floor=n
        return real_floor
