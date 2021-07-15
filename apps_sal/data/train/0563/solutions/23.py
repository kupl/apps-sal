try:
    def fun(N,coins,q1,q2):
        arr=coins[q1-1:q2]
        return sum(arr)
    
    
    T=int(input())
    for _ in range(T):
        N=int(input())
        coins = [int(i) for i in input().split()]
        q = int(input())
        for i in range(q):
            q1,q2 = list(map(int,input().split()))
            print(fun(N,coins,q1,q2))
        
except:
    pass

