from collections import defaultdict
from heapq import heappop, heappush
from typing import List, Tuple


def shortest(N: int, edgeList: List[Tuple[int, int, int]]) -> int:
    graph = defaultdict(list)
    for (v, u, e) in edgeList:
        graph[v].append((u, e))
    pathes = defaultdict(lambda: float('inf'), {0: 0})
    queue = [(0, 0)]
    while queue:
        (cost, v) = heappop(queue)
        if v == N - 1:
            return cost
        for (u, e) in graph[v]:
            new_cost = cost + e
            if new_cost < pathes[u]:
                pathes[u] = new_cost
                heappush(queue, (new_cost, u))
    return -1
