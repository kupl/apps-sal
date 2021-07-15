def seven(m):
    a=0
    while(m>95):
        m=str(m)
        m=int(m[:-1])-int(m[-1])*2
        a=a+1
        if(m%7==0 and m<70):
            break
    return (m,a)
