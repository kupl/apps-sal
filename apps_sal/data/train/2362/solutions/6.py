for _ in range(int(input())):
    n = int(input())
    (maxx, minx) = (100000, -100000)
    (maxy, miny) = (100000, -100000)
    for _ in range(n):
        (xi, yi, d, r, u, l) = tuple(map(int, input().split()))
        if d == 0:
            minx = xi if xi > minx else minx
        if r == 0:
            maxy = yi if yi < maxy else maxy
        if u == 0:
            maxx = xi if xi < maxx else maxx
        if l == 0:
            miny = yi if yi > miny else miny
    if miny <= maxy and minx <= maxx:
        print(1, minx, miny)
    else:
        print(0)
