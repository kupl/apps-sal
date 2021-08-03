def get_real_floor(n):
    if n <= 0:
        return n
    elif(n > 0 and n != 13 and n < 14):
        return (n - 1)
    else:
        return(n - 2)
