t = int(input())
for _ in range(t):
    x, y = list(map(int, input().split()))
    p = 0
    mx = max(x, y)
    while 2**p <= mx:
        p += 1
    px = p
    py = p
    x_m = 0
    y_m = 0
    x += 1
    y += 1
    while x:
        while 2**px > x:
            px -= 1
        x -= 2**px
        x_m += 1
    while y:
        while 2**py > y:
            py -= 1
        y -= 2**py
        y_m += 1
    if x_m == y_m:
        print(0, 0)
    else:
        if x_m > y_m:
            print(2, abs(x_m - y_m))
        else:
            print(1, abs(x_m - y_m))
