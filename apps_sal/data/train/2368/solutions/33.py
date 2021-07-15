t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ma=min(a)
    mb=min(b)
    ans=0
    for i in range(n):
        ga=a[i]-ma 
        gb=b[i]-mb 
        ans=ans+max(ga,gb)
    print(ans)
