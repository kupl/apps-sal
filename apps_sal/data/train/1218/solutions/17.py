t=int(input())
for _ in range(t):
    ans=0
    x,n=map(int,input().split())
    for i in range(x,n,x):
        ans=ans+i
    print(ans)
