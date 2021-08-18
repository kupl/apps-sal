from heapq import heappop, heappush

N, Q = map(int, input().split())


event = []
q = []
for _ in range(N):
    S, T, X = map(int, input().split())
    event.append([S - X, 1, X])
    event.append([T - X, -1, X])

for i in range(Q):
    event.append([int(input()), 2, i])

stop_set = set()
event.sort()
q = []

for pos, m, x in event:
    if m == -1:
        stop_set.remove(x)

    elif m == 1:
        heappush(q, x)
        stop_set.add(x)

    else:
        while q:
            if q[0] not in stop_set:
                heappop(q)
            else:
                break

        if q:
            print(q[0])
        else:
            print(-1)
