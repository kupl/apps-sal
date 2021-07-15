# cook your dish here

t = int(input())
for rep in range(t):
    h,x,y = list(map(int,input().split()))
    req = h - 1
    mini = 1000000000
    g = 0
    t = 0
    base = x
    f = 0
    while base <= req:
        if req % base == 0:
            f = 1
            t = req // base
            if g + t < mini:
                mini = g + t
        base = base + y
        g = g + 1
    if f == 1:
        print(mini)
    else:
        print(-1)

