from heapq import heappush, heappop
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
(N, Q) = list(map(int, input().split()))
STX = [[int(x) for x in input().split()] for _ in range(N)]
EVENT = []
for (s, t, x) in STX:
    EVENT.append((s - x, 1, x))
    EVENT.append((t - x, 0, x))
for i in range(Q):
    d = int(input())
    EVENT.append((d, 2, i))
ans = [-1] * Q
EVENT.sort()
STOP = set()
h = []
for (t, op, x) in EVENT:
    if op == 2 and STOP:
        while h and h[0] not in STOP:
            heappop(h)
        ans[x] = h[0]
    elif op == 1:
        STOP.add(x)
        heappush(h, x)
    elif op == 0:
        STOP.remove(x)
print('\n'.join(map(str, ans)))
