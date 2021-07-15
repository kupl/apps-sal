t=int(input())
for i in range(t):
    n=int(input())
    A=list(map(int,input().split()))
    m=int(input())
    x=n//2
    u=0
    te=-1
    while(x):
        te=A[u]
        A[u]=A[u+1]
        A[u+1]=te
        u+=2
        x-=1
    for j in range(n):
        A[j]+=(A[j]%3)
    for j in range(n):
        u=j
        v=n-j-1
        te=A[u]
        A[u]=A[v]
        A[v]=te
    mi=-1
    ma=-1
    A.sort()
    for j in range(n):
        if(A[j]>m):
            ma=A[j]
            break
    A=A[: : -1]
    for j in range(n):
        if(A[j]<m):
            mi=A[j]
            break
    print(mi,ma)
