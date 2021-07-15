try:
    n,k=map(int,input().split()) 
    p=1000000007
    a=[int(x) for x in input().split()]
    b=a.copy()
    for i in range(k):
        for j in range(n):
            s=0
            for m in range(j+1):
                s+=a[m]
            b[j]=s
        a=b.copy()
    for o in range(n):
        b[o]=b[o]%p
        print(b[o],end=' ')
except:
    pass
