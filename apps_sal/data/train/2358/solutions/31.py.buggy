import heapq
xs, ys, xt, yt = list(map(int, input().split()))
N = int(input())
XY = [tuple(map(int, input().split())) for i in range(N)]
D = [[0] * (N + 2) for i in range(N + 2)]
XY.append((xs, ys, 0))
XY.append((xt, yt, 0))


for i in range(N + 1):
    x1, y1, r1 = XY[i]
    for j in range(i + 1, N + 2):
        x2, y2, r2 = XY[j]
        d = (x1 - x2)**2 + (y1 - y2)**2
        d = d ** (0.5)
        D[i][j] = max(0, d - r1 - r2)
        D[j][i] = D[i][j]
hq = []
hq.append((0, N))
s = set([i for i in range(N + 2)])

while(hq):

    c, x = heapq.heappop(hq)
    if x == N + 1:
        print(c)
        return
    if x in s:

        s.remove(x)
    else:
        continue
    for i in s:
        heapq.heappush(hq, (c + D[x][i], i))
