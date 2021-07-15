def primeFactors(n):
    s=str()
    for i in range(2, int(n**(1/2))+1):
        j=0
        while n/i%1==0.0:
            j+=1
            n/=i
        if j>1:
            s+="("
            s+=str(i)
            s+="**"
            s+=str(j)
            s+=")"
        if j==1:
            s+="("
            s+=str(i)
            s+=")"
    if n!=1:
        s+="("
        s+=str(int(n))
        s+=")"
        return s         
    else:
        return s        
