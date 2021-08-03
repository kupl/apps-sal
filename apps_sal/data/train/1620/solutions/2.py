from collections import deque
from heapq import heappush, heappop


def n_linear(m, n):
    y, h, q = 1, [], {}
    for x in m:
        h.append((y, x))
        q[x] = deque([x * y + 1])
    while n:
        z, w = heappop(h)
        if y != z:
            y = z
            for x in m:
                q[x].append(x * y + 1)
            n -= 1
        heappush(h, (q[w].popleft(), w))
    return y
