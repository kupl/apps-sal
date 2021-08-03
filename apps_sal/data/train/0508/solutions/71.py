import heapq
import sys
input = sys.stdin.readline
read = sys.stdin.read

n, q = map(int, input().split())
STX = [list(map(int, input().split())) for _ in range(n)]
D = list(map(int, read().split()))
E = []
for s, t, x in STX:
    E.append((s - x, x, 1))
    E.append((t - x, x, 0))
E.sort(reverse=True)
que = []
stop = set()
que.append(10**10)
stop.add(10**10)
for d in D:
    while E and E[-1][0] <= d:
        temp, x, f = E.pop()
        if f:
            heapq.heappush(que, x)
            stop.add(x)
        else:
            stop.remove(x)
    while que[0] not in stop:
        heapq.heappop(que)
    if que[0] == 10**10:
        print(-1)
    else:
        print(que[0])
