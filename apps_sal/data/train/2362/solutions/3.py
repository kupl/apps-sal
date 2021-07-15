q = int(input())
for _ in range(q):
    n = int(input())
    lm = dm = -100000
    rm = um = 100000
    for _ in range(n):
        x, y, l, u, r, d = list(map(int, input().split()))
        if l == 0:
            lm = max(lm, x)
        if r == 0:
            rm = min(rm, x)
        if u == 0:
            um = min(um, y)
        if d == 0:
            dm = max(dm, y)
    if lm > rm or um < dm:
        print(0)
    else:
        print(1, lm, dm)


