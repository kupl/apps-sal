for _ in range(int(input())):
    n,d=list(map(int,input().split()))
    l=list(map(int,input().split()))
    i=n-1
    cv=d
    while(i>=0):
        q=cv//l[i]
        cv=l[i]*q
        i-=1
    print(cv)




