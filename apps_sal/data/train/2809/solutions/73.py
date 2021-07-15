def digitize(n):
    x=list(str(n))
    y=[]
    for i in range(len(x)-1,-1,-1):
        y.append(int(x[i]))
    return y
