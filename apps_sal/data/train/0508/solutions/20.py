from heapq import heapify, heappop, heappush
from collections import defaultdict
import sys
input = sys.stdin.readline
INF = 1 << 31
(N, Q) = map(int, input().split())
event = []
for _ in range(N):
    (s, t, x) = map(int, input().split())
    event.append((s - x, -1, x))
    event.append((t - x, 0, x))
for i in range(Q):
    d = int(input())
    event.append((d, 1, i))
q = []
ans = [-1] * Q
event.sort()
push = defaultdict(int)
pop = defaultdict(int)
for i in range(2 * N + Q):
    (t, typ, x) = event[i]
    if typ == -1:
        heappush(q, x)
        push[x] += 1
    elif typ == 0:
        pop[x] += 1
    else:
        p = -1
        if q:
            p = q[0]
        while p != -1 and push[p] - pop[p] == 0:
            heappop(q)
            if q:
                p = q[0]
            else:
                p = -1
                break
        ans[x] = p
print('\n'.join(map(str, ans)))
