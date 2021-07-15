t=int(input())
for i in range(t):
    n,k,x=map(int,input().split())
    X=[x]
    for i in range(0,k-1):
        X.append(0)
    i=0
    v=[]
    j=0
    while(j<n):
        v.append(X[i])
        i+=1
        if i==len(X):
            i=0
        j+=1
    print(*v)
        
