for t in range(int(input())):
    d,m = [int(i) for i in input().split()]
    tot = 0
    p = 1
    while p<=d:
        p *= 2
    p //= 2
    while d>0:
        tot += (d-p+1)*(tot+1)
        tot %= m
        d = p-1
        p //= 2
    print(tot)

