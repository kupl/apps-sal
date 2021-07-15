def difference_of_squares(n):
    a=0
    b=0
    for i in range (1,n+1):
        a=a+i
        b=b+i**2
    return a**2 - b

