import heapq

N, Q = map(int, input().split())

events = []

for _ in range(N):
    S, T, X = map(int, input().split())

    events.append([S - X, 1, X])
    events.append([T - X, 0, X])

for _ in range(Q):
    D = int(input())
    events.append([D, 2, 0])

events.sort()

closed = set()
que = []

idx = 0
for time, flag, position in events:
    if flag == 0:
        closed.remove(position)
    elif flag == 1:
        heapq.heappush(que, position)
        closed.add(position)
    else:
        while len(que) > 0 and que[0] not in closed:
            heapq.heappop(que)

        if len(que) > 0:
            print(que[0])
        else:
            print(-1)
