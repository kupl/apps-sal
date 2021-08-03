from heapq import *


def n_linear(m, n):
    k = [1]
    queue = []
    while len(k) <= n:
        for x in m:
            heappush(queue, x * k[-1] + 1)
        k.append(heappop(queue))

        while queue[0] == k[-1]:
            heappop(queue)

    return k[-1]
