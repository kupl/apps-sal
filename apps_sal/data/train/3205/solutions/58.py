def is_divisible(n,x,y):
    x1 = n % x
    y1 = n % y
    if (x1 >= 1 or y1 >= 1):
        return(False)
    elif (x1 == 0 and y1 == 0):
        return (True)
