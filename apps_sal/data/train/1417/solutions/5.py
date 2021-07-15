for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=[0 for x in range(11)]
    for i in a:
        b[i]+=1
    ans=b[1]
    for i in range(1,9):
        ans=min(ans,b[i])
    print(ans)
