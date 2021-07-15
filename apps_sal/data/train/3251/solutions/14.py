def primeFactors(n):
    if isinstance(((n+1)/6),int) or isinstance(((n-1)/6),int): return n
    g=n
    pf=''
    prime=2
    while g!=1:
        count=0
        if (prime-1)%6==0 or (prime+1)%6==0 or prime==2 or prime==3:
            while g%prime==0:
                g=g/prime
                count+=1
            if count>1:
                pf=pf+'('+str(prime)+'**'+str(count)+')'
            elif count>0:
                pf=pf+'('+str(prime)+')'
        prime+=1
    return pf
