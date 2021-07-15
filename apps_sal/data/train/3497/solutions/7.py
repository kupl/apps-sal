def isPP(n):
    b=n
    import math
    root=math.sqrt(n)
    iroot=int(root)
    if float(iroot)==root:
        return([iroot,2])
    elif n==1:
        return([1,1])
    else:
        if iroot==2:
            iroot=3
        for i in range(2,iroot):
            s=0
            d='no'
            n=b
            while n%i==0:
                d='yes'
                n=n/i
                s=s+1
                if n==1:
                    return([i,s])
            else:
                d='no'
        if d=='no':
            return None
    
                

