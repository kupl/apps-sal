from heapq import heappush, heappop
(N, Q) = list(map(int, input().split()))
(l, q) = ([], [])
u = set()
for _ in range(N):
    (S, T, X) = list(map(int, input().split()))
    l.append((S - X, 1, X))
    l.append((T - X, 0, X))
for i in range(Q):
    l.append((int(input()), 2, i))
l.sort()
for (_, m, x) in l:
    if m == 0:
        u.remove(x)
    elif m == 1:
        heappush(q, x)
        u.add(x)
    else:
        while q:
            if q[0] not in u:
                heappop(q)
            else:
                break
        print(q[0] if q else -1)
