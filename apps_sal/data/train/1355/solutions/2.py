for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=[0 for i in range(n)]
    for i in range(n):
        if a[i]<=n:
            ans[i]=a[i]+a[a[i]-1]
        else:
            x=a[i]
            while x>=n:
                x//=2
            ans[i]=a[n-x-1]
    print(*ans)
