def growing_plant(u,d,de):
    n=0
    m=0
    while de>=n:
        m+=1
        n+=u
        if n>=de:
            break
        n-=d
    return m
