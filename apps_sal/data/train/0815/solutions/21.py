# cook your dish here
from collections import deque
primes = {2, 3, 5, 7, 11, 13, 17}
edges = [(0, 3), (0, 1), (1, 2), (1, 4), (2, 5), (3, 4), (3, 6), (4, 5), (4, 7), (5, 8), (6, 7), (7, 8)]
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
avail = {tuple(x): 0}
q = deque([x])
while q:
    curr = q.popleft()
    for e in edges:
        if curr[e[0]] + curr[e[1]] in primes:
            nxt = curr[0:]
            nxt[e[0]], nxt[e[1]] = nxt[e[1]], nxt[e[0]]
            nxtt = tuple(nxt)
            if nxtt not in avail:
                avail[nxtt] = avail[tuple(curr)] + 1
                q.append(nxt)
t = int(input())
while t:
    inp = input()
    grid = []
    for i in range(3):
        inp = input()
        for j in inp.strip().split(" "):
            grid.append(int(j))
    gridt = tuple(grid)
    if gridt in avail:
        print(avail[gridt])
    else:
        print(-1)
    t -= 1
