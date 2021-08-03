from heapq import *


def n_linear(ms, n):
    lst = [1] * (n + 1)
    q = [(1 + v, v, 1) for v in ms]
    heapify(q)
    for i in range(1, n + 1):
        v, x, j = heappop(q)
        lst[i] = v
        heappush(q, (lst[j] * x + 1, x, j + 1))
        while q[0][0] == lst[i]:
            v, x, j = heappop(q)
            heappush(q, (lst[j] * x + 1, x, j + 1))
    return lst[n]
