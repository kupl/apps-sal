def find_multiples(integer, limit):
    l=[]
    for x in range(1,limit+1):
        z=integer*x
        if z<=limit:
            l.append(z)
        else:
            break
    return l

