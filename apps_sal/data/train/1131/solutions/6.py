for _ in range(int(input())):
    n,k=[int(x) for x in input().split()]
    a=list(map(int,input().split()))
    dp=[0]*(max(a)+1)
    for _ in range(n):
        dp[a[_]]+=1
    for _ in range(1,len(dp)):
        if dp[_]>k:
            print(_,end=" ")
    print()        
        
