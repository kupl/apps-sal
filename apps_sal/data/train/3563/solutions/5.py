def distance(n):
    if n==1:
        return 0
    i=1
    while(True):
        if n<=(2*i-1)**2:
            break
        i+=1
    x=(n-(2*i-3)**2-1)%(2*i-2)
    h=(2*i-2)//2
    if x<h:
        return i+h-x-2
    else:
        return i+x-h
