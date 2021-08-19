from heapq import heappush, heappop, heapify
N = int(input())
P = []
for i in range(N):
    (x, y) = map(int, input().split())
    P.append((x, y) if x < y else (y, x))
X = [x for (x, y) in P]
Y = [y for (x, y) in P]
MIN = min(X)
MAX = max(Y)
res = (max(X) - MIN) * (MAX - min(Y))
base = MAX - MIN
heapify(P)
r = max(X)
while P:
    (x, y) = heappop(P)
    res = min(res, base * (r - x))
    if y != -1:
        heappush(P, (y, -1))
        r = max(r, y)
    else:
        break
print(res)
