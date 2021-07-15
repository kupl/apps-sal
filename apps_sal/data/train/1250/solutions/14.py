T=int(input())
while T>0:
    T-=1
    n=int(input())
    ans=0;
    for i in range(n+1):
        for j in range(n-i+1):
            k=(n-i-j)
            # print(i,j,k)
            ans+=((pow(2,j,1000000007)*pow(3,k,1000000007))%1000000007)
    print(ans)

