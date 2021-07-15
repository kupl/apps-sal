for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=[1]*(n)
    f=1
    ind=0
    if a[0]==a[1]:
        ind=1
    for i in range(1,n):
        if a[i]==a[i-1]:
            ans[i]=ans[i-1]
        else:
            ans[i]=3-ans[i-1]
            f=2
        if a[i]==a[(i+1)%n]:
            ind=(i+1)%n
        
    if a[0]!=a[-1] and ans[-1]==ans[0]:
        ans[-1]=3
        f=3
    
    # print(ind)
    
    if f==3 and ind:
        for i in range(ind,n):
            ans[i]=3-ans[i]
        ans[-1]=3-ans[0]    
            
    
    print(len(set(ans)))    
    
    
    # if f:
    #     print(3)
        
    # else:
    #     print(2)
    print(*ans)    
