import heapq
(N, Q) = list(map(int, input().split()))
(S, T, X) = ([], [], [])
Ev = []
for _ in range(N):
    (s, t, x) = list(map(int, input().split()))
    Ev.append((s - x, True, x))
    Ev.append((t - x, False, x))
'\n2 5 6\n5 -1\n4 2\n3 3\n2 4\n1 5\n0 -1\n'
Ev.sort()
h = []
closed = set()
eidx = 0
for i in range(Q):
    d = int(input())
    while eidx < 2 * N and Ev[eidx][0] <= d:
        (t, e, x) = Ev[eidx]
        eidx += 1
        if e:
            heapq.heappush(h, x)
            closed.add(x)
        else:
            closed.remove(x)
    while h and h[0] not in closed:
        heapq.heappop(h)
    if h:
        print(h[0])
    else:
        print(-1)
