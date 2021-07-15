test=int(input())
for _ in range(test):
    n,k=map(int,input().split())
    ans=pow(n,2,1000000007)
    k=k-1
    i=0
    while(k!=0):
        ans+=(2*n)%1000000007
        if n!=0:
            k-=1
        if k==0:
            break
        ans+=(i+2)%1000000007
        k-=1
        
        i=i+2
    print(ans%1000000007)
