def primeFactors(n):
    factors=[]
    n1=n
    while n1%2 == 0:
        n1=n1/2
        factors.append(2)
    for i in range (3, int(n1**(1/2.0))):
        while n1%i == 0:
            n1=n1/i
            factors.append(i)
    if factors==[]:
        factors.append(n)
    elif n1 != 1:
        factors.append(int(n1))
    factors.append(0)
    x=0
    l=''
    final=""
    for a in factors:
        if l=='':
            l=a
            x=x+1
        elif l != a:
            if x==1:
                final=final+"("+str(l)+")"
                l=a
                x=1
            else:
                final=final+"("+str(l)+"**"+str(x)+")"
                l=a
                x=1
        else:
            x=x+1
    return final
            

