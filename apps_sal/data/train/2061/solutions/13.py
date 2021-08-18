import sys
input = sys.stdin.readline
n = int(input())
C = [list(map(int, input().split())) for i in range(n)]

big = 10**5
l = 7
D = [[[big] * 4 for i in range(l)] for j in range(l)]
mi = 3

D[mi][mi][0] = 0

L = [(0, 1, 1), (1, 0, 3), (1, 1, 2), (0, 1, 2), (1, 0, 2), (0, 0, 3), (0, 0, 1)]
LL = [(0, 1, 1), (1, 0, 3), (1, 1, 2), (0, 1, 2), (1, 0, 2), (0, 0, 3), (0, 0, 1), (0, 0, 0)]


Q = [(mi, mi, 0, 0)]
s = 0
while s < len(Q):
    x, y, t, d = Q[s]
    for nx, ny, nt in L:
        for k in range(t):
            nx, ny = ny, -nx
        tt = (nt + t) % 4
        xx = x + nx
        yy = y + ny
        if 0 <= xx < l and 0 <= yy < l and D[xx][yy][tt] == big:
            D[xx][yy][tt] = d + 1
            Q.append((xx, yy, tt, d + 1))
    s += 1

for i in range(n):
    t = -1
    Xs = [C[i][0], C[i][2], C[i][4]]
    Ys = [C[i][1], C[i][3], C[i][5]]
    Xs.sort()
    Ys.sort()
    MX = max(Xs)
    mX = min(Xs)
    MY = max(Ys)
    mY = min(Ys)
    if Xs[1] == MX and Ys[1] == MY:
        t = 2
    elif Xs[1] == mX and Ys[1] == mY:
        t = 0
    elif Xs[1] == MX and Ys[1] == mY:
        t = 3
    else:
        t = 1
    cx, cy = Xs[1], Ys[1]
    ans = float("inf")
    c = 0
    for nx, ny, nt in LL:
        for k in range(t):
            nx, ny = ny, -nx
        tt = (nt + t) % 4
        xx = cx + nx
        yy = cy + ny
        for j in range(l):
            for k in range(l):
                if (tt % 2 == 0 and (j - mi - xx) * (k - mi - yy) <= 0) or (tt % 2 == 1 and (j - mi - xx) * (k - mi - yy) >= 0):
                    dx = abs(j - mi - xx)
                    dy = abs(k - mi - yy)
                    Md = max(dx, dy)
                    p = 0
                    if c != len(LL) - 1:
                        p = 1
                    nans = D[j][k][tt] + Md * 2 + p
                    ans = min(ans, nans)
        c += 1
    print(ans)
