def f(n):
    if n==1:
        return 1
    elif n == 0:
        return 0
    
    a,b = 1,2
    for i in range(0,n-2):
        a,b = b,a+b+1
    return b
