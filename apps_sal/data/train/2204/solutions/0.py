import heapq
import sys
input = sys.stdin.readline
mod = 998244353
(n, m) = list(map(int, input().split()))
E = [[] for i in range(n + 1)]
E2 = [[] for i in range(n + 1)]
for i in range(m):
    (x, y) = list(map(int, input().split()))
    E[x].append(y)
    E2[y].append(x)
TIME = [1 << 29] * (n + 1)
TIME[1] = 0


def shuku(x, y):
    return (x << 20) + y


Q = []
ANS = []
for k in range(n + 1):
    NQ = []
    if k <= 1:
        heapq.heappush(Q, shuku(0, 1))
    if k % 2 == 0:
        while Q:
            x = heapq.heappop(Q)
            time = x >> 20
            town = x - (time << 20)
            if TIME[town] < time:
                continue
            for to in E[town]:
                if TIME[to] > time + 1:
                    TIME[to] = time + 1
                    heapq.heappush(Q, shuku(TIME[to], to))
                    heapq.heappush(NQ, shuku(TIME[to], to))
    else:
        while Q:
            x = heapq.heappop(Q)
            time = x >> 20
            town = x - (time << 20)
            if TIME[town] < time:
                continue
            for to in E2[town]:
                if TIME[to] > time + 1:
                    TIME[to] = time + 1
                    heapq.heappush(Q, shuku(TIME[to], to))
                    heapq.heappush(NQ, shuku(TIME[to], to))
    Q = NQ
    ANS.append(TIME[n])
    if k >= 100 and TIME[n] != 1 << 29:
        break
A = ANS[0]
for k in range(1, len(ANS)):
    if ANS[k] == 1 << 29:
        continue
    if ANS[k - 1] == 1 << 29:
        A = (ANS[k] + pow(2, k, mod) - 1) % mod
    if k < 60 and ANS[k - 1] - ANS[k] > pow(2, k - 1):
        A = (ANS[k] + pow(2, k, mod) - 1) % mod
print(A)
