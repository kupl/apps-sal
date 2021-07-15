def get_real_floor(n):
    return n-1 if n<13 and n>0 else n if n<=0 else n-2 if n>13 else n
