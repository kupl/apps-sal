def factor_sum(n):
    while True:
        i=2
        s=0
        a=n
        while i<=n:
            if n%i==0:
                s+=i
                n/=i
                if n==1:
                    break
            else:
                i+=1
                
        if a!=s:
            n=s
        else:
            return s
