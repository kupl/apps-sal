import sys
from operator import itemgetter
from heapq import heapify, heappush, heappop

read = sys.stdin.read

N, Q, *STXD = list(map(int, read().split()))
STX = STXD[:3 * N]
queue = []

for i, (S, T, X) in enumerate(zip(*[iter(STX)] * 3), 1):
    queue.append((S - X - 0.5, X, i))
    queue.append((T - X - 0.5, -X, i))

for D in STXD[3 * N:]:
    queue.append((D, 0, 0))

queue.sort(key=itemgetter(0), reverse=True)
heap = []
heapify(heap)
stop, construction = -1, 0
not_available = set()
while queue:
    _, x, n = queue.pop()
    if x == 0:
        print(stop)
    elif x < 0:
        not_available.add(n)
        if n == construction:
            while heap:
                stop, construction = heappop(heap)
                if construction not in not_available:
                    break
            else:
                stop, construction = -1, 0
    else:
        if stop != -1:
            if stop <= x:
                heappush(heap, (x, n))
            else:
                heappush(heap, (stop, construction))
                stop, construction = x, n
        else:
            stop, construction = x, n

