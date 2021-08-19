import sys
import numpy as np
from collections import deque


def readline(): return list(map(int, sys.stdin.readline().replace("\n", "").split(" ")))


(T,) = readline()


def run():
    N, M = readline()
    grid = np.full((N, M), -1)
    queue = deque()

    (X,) = readline()
    for _ in range(X):
        (x, y) = readline()
        (x, y) = (x - 1, y - 1)
        queue.append((x, y))
        grid[x, y] = 0

    (Y,) = readline()
    for _ in range(Y):
        (x, y) = readline()
        (x, y) = (x - 1, y - 1)
        grid[x, y] = -2

    while(len(queue) > 0):
        (x, y) = queue.popleft()
        #print('Propagate', (x+1,y+1), '; d =', grid[x,y])
        for (u, v) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if u < 0 or v < 0 or u >= N or v >= M:
                continue
            if grid[u, v] == -1:
                grid[u, v] = grid[x, y] + 1
                queue.append((u, v))

    def val(x): return str(x) if x != -2 else 'X'

    for i in range(N):
        print(' '.join(val(grid[i, j]) for j in range(M)))


for _ in range(T):
    run()
