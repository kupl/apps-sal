t=int(input())
for _ in range(t):
    n,m,k=list(map(int,input().strip().split()))
    a=list()
    for i in range(n):
        b=list(map(int,input().strip().split()))
        a.append(b)
    sm1,sm2=0,0
    for i in range(n):
        for j in range(k):
            sm2+=a[i][j]
        if sm2>sm1:
            sm1=sm2
        for j in range(k,m):
            sm2+=(a[i][j]-a[i][j-k])
            if sm2>sm1:
                sm1=sm2
        sm2=0
    for i in range(m):
        for j in range(k):
            sm2+=a[j][i]
        if sm2>sm1:
            sm1=sm2
        for j in range(k,n):
            sm2+=(a[j][i]-a[j-k][i])
            if sm2>sm1:
                sm1=sm2
        sm2=0
    print(sm1)

