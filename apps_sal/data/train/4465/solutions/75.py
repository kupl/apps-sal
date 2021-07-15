def super_size(n):
    a=[0,0,0,0,0,0,0,0,0,0]
    while n>=1:
        a[n%10]+=1
        n//=10
    ans=0
    for i in range(9,-1,-1):
        while a[i]:
            ans*=10
            ans+=i
            a[i]-=1
    return ans
