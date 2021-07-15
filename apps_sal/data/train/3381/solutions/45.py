def get_real_floor(n):
    if n<0: return n
    elif n>0 and n<13: return n-1
    elif n==0: return 0
    else: return n-2
