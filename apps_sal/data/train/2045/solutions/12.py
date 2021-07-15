def ans():
    n,m = list(map(int,input().split()))
    res,alive = [0]*n,[(i+1) for i in range(n+2)]
    from sys import stdin
    for _ in range(m):
        l,r,x = list(map(int,stdin.readline().split()))
        i=l
        while i<=r:
            if res[i-1]==0 and i!=x:
                res[i-1] = x
            temp = alive[i]
            if i < x:
                alive[i] = x
            else:
                alive[i] = r+1
            i = temp
    print(*res)
ans()

