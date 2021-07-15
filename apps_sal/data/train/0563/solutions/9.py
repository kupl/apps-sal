for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    q=int(input())
    for i in range(q):
        x,y=map(int,input().split())
        ans=sum(a[x-1:y])
        print(ans)
