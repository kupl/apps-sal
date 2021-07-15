for t in range(int(input())):
    n,m,k=list(map(int,input().split(' ')))
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split(' '))))
    max=0
    b=[0 for i in range(n)]
    c=[0 for i in range(m)]
    for i in range(n):
        b[i]=sum(a[i][:k])
        if b[i]>max:
            max=b[i]
    for i in range(m):
        g=0
        for x in range(k):
            g=g+a[x][i]
        c[i]=g
        if g>max:
            max=g
    #print(b,c)
    for i in range(n):
        for j in range(1,m-k+1):
            b[i]=b[i]+a[i][j+k-1]-a[i][j-1]
            #print(b[i])
            if b[i]>max:
                max=b[i]
    for i in range(m):
        for j in range(1,n-k+1):
            c[i]=c[i]+a[j+k-1][i]-a[j-1][i]
            if c[i]>max:
                max=c[i]

    print(max)
    

