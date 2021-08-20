import sys
input = sys.stdin.readline
Q = int(input())
for _ in range(Q):
    N = int(input())
    (minx, miny, maxx, maxy) = (-10 ** 5, -10 ** 5, 10 ** 5, 10 ** 5)
    for __ in range(N):
        (X, Y, L, U, R, D) = list(map(int, input().split()))
        if L == 0:
            minx = max(minx, X)
        if R == 0:
            maxx = min(maxx, X)
        if U == 0:
            maxy = min(maxy, Y)
        if D == 0:
            miny = max(miny, Y)
    if maxx >= minx and maxy >= miny:
        print(1, minx, miny)
    else:
        print(0)
