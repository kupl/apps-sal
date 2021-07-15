def pattern(n):
    c=str()
    for i in range(1,n+1):
        if i == n:
            c=c+i*str(i)
        else:
            c=c+i*str(i)+"\n"
    return c
