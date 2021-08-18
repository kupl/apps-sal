import heapq
import sys
input = sys.stdin.readline

N, Q = list(map(int, input().split()))

S, T, X = [], [], []

Ev = []
for _ in range(N):
    s, t, x = list(map(int, input().split()))
    Ev.append((s - x, True, x))
    Ev.append((t - x, False, x))
"""
2 5 6
5 -1
4 2
3 3
2 4
1 5
0 -1
"""
Ev.sort()
h = []
closed = set()
eidx = 0
D = []

for i in range(Q):
    D.append(int(input()))

for d in D:
    while eidx < 2 * N and Ev[eidx][0] <= d:
        t, e, x = Ev[eidx]
        eidx += 1
        if e:
            heapq.heappush(h, x)
            closed.add(x)
        else:
            closed.remove(x)

    while h and h[0] not in closed:
        heapq.heappop(h)

    if h:
        print((h[0]))
    else:
        print((-1))
