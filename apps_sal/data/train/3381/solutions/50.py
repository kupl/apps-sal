def get_real_floor(n):
    # code here
    if n<0:
        return n
    elif n>0 and n<=12:
        return n-1
    elif  n>12 :
        return n-2
    else:
        return 0 
        

