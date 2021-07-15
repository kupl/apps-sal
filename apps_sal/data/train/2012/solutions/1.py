n=int(input())

L=[0]*(n+1)

X=[False]*(n+1)

if(n%4!=0 and n%4!=1):
    print(-1)

else:
    for i in range(1,n+1):
        if(X[i]):
            continue
        X[i]=True
        X[n-i+1]=True
        for j in range(i+1,n+1):
            if(X[j]):
                continue
            X[j]=True
            X[n-j+1]=True
            L[i]=j
            L[n-i+1]=n-j+1
            L[j]=n-i+1
            L[n-j+1]=i
            break
        if(n%4==1):
            L[n//2+1]=n//2+1
    for i in range(1,n):
        print(L[i],end=" ")
    print(L[n])
        

