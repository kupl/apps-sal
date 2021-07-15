def get_real_floor(n):
    if n == 0 or n ==1:
        print((0))
        return 0
    if n<13 and n>1:
        print((n-1))
        return n-1
    if n>13:
        print((n-2))
        return n-2
    return n

