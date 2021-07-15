def test():
    N=int(input())
    ls=list(map(int,input().split()))
    ans=0
    n=N/2
    for each in ls:
        if each>=n:
            ans+=1
    print(ans)

T=int(input())
for i in range(T):
    test()

