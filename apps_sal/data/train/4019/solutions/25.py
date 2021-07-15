def max_multiple(d, b):
    l=0
    for i in range(d,b+1):
        if i%d==0:
            if i>l:
                l=i
    return l
