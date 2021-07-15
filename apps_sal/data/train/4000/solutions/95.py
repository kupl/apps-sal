def strong_num(n):
    print(n)
    g=[]
    z=[int(x) for x in str(n)]
    print(z)
    for i in z:
        if i >= 0:
            fac=1
            for y in range(1,i+1):
                fac=fac*y
                
            g.append(fac)
    print(g)
    h=sum(g)  
    if h == n:
        mystr="STRONG!!!!"
    if h!=n:
        mystr="Not Strong !!"
    
    return mystr
