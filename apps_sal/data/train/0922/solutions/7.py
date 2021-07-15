for _ in range(int(input())):
    n,m=[int(x) for x in input().split()]
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    x=a+b
    dp=[0]*(max(x)+1)
    for _ in range(len(x)):
        dp[x[_]]+=1
    for _ in range(1,len(dp)):
        if dp[_]==1:
            print(_,end=" ")
    print()        
        
    
    
