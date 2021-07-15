T=int(input())
res=[]
for i in range (T):
    lis=[]
    s=input()
    s=list(s.split())
    x=int(s[0])
    k=int(s[1])
    fac=[]
    po=[]
    
    n=0
    m=0
    for j in range (2,x+1):
        if (x%j==0):
            n+=(j**k)
    fac.append(n)
    for j in range (2,k+1):
        if (k%j==0):
            m+=(j*x)
    fac.append(m)
    res.append(fac)
for i in range (T):
    print(res[i][0], res[i][1])

