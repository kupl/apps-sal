from math import *
t=int(input())
p=10**9+7
for i in range(t):
    
    
    n,k=list(map(int,input().split()))
    ans=(n+ceil((k-1)/2))%p
    r=ans
    
    ans=(((((ans+1)*(ans))//2)*2))%p
    
    
    if(k==0):
        print(0)
        continue
    k=k-1
    if(n==0):
        print((((k*(k+1))//2)*2)%p)
        continue

    if(k!=0):
        if(k%2==0):
            ans=ans-(r-(r-n))
        
        else:
            ans=ans-r-(r-n)
    else:
        ans=ans-r
    print(ans%p)

