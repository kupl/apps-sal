import sys
def input(): return sys.stdin.readline().strip()


T = int(input())
for _ in range(T):
    n = int(input())
    minx = -(10**5)
    maxx = 10**5
    miny = -(10**5)
    maxy = 10**5
    for i in range(n):
        x, y, f1, f2, f3, f4 = list(map(int, input().split()))
        if f1 == 0:
            minx = max(minx, x)
        if f2 == 0:
            maxy = min(maxy, y)
        if f3 == 0:
            maxx = min(maxx, x)
        if f4 == 0:
            miny = max(miny, y)
    if minx > maxx or miny > maxy:
        print(0)
    else:
        print(1, minx, miny)
