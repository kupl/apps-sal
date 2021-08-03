inf = 100000
for q in range(int(input())):
    n = int(input())
    l, u, r, d = -inf, inf, inf, -inf
    for i in range(n):
        x, y, f1, f2, f3, f4 = list(map(int, input().split()))
        if f1 == 0:
            l = max(l, x)
        if f2 == 0:
            u = min(u, y)
        if f3 == 0:
            r = min(r, x)
        if f4 == 0:
            d = max(d, y)
    if d > u or l > r:
        print(0)
    else:
        print(1, l, d)
