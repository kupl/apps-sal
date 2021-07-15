for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ma=min(a)
    mb=min(b)
    ans=0
    for i in range(n):
        f=min(a[i]-ma,b[i]-mb)
        ans+=f
        a[i]-=f
        b[i]-=f
        ans+=b[i]-mb+a[i]-ma
    print(ans)

