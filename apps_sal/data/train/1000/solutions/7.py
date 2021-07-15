try:
    t=int(input())
    for _ in range(t):
        n=int(input())
        l=list(map(int,input().split()))
        x=min(l)
        if(n//x == n/x):
            print(n//x)
        else:
            print((n//x)+1)
except:
    pass

