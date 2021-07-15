def hotpo(n):
    res=0
    for i in range(0,500):
        if n==1:
            return res
        elif n%2==0:
            n/=2
            res+=1
        else:
            n=n*3+1
            res+=1

