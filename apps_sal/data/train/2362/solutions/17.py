q = int(input())
for i in range(q):
    n = int(input())
    l = -100000
    t = 100000
    r = 100000
    b = -100000
    for j in range(n):
        x, y, f1, f2, f3, f4 = list(map(int, input().split()))
        if f1 == 0:
            if l <= x:
                l = x
        if f2 == 0:
            if t >= y:
                t = y
        if f3 == 0:
            if r >= x:
                r = x
        if f4 == 0:
            if b <= y:
                b = y
    cx,cy=None,None
    ans = 1
    if l <= r:
        cx = l
    else:
        ans =0
    if b <= t:
        cy = b
    else:
        ans = 0
    if ans == 0:
        print(ans)
    else:
        print(ans, cx, cy)


