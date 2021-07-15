import math
for _ in range(int(input())):
    n=int(input())
    if n==1:
        print(0)
    else:
        k=int(n**(0.5))
        if k*k<n:
            k+=1
        # print(n,k)    
        ans=k-1
        if k*(k-1)>=n:
            ans+=(k-2)
        else:
            ans+=(k-1)
        print(ans)    
