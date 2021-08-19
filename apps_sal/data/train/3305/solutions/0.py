import heapq
from collections import defaultdict


def shortest(N, edge):
    (ver, inf) = (defaultdict(list), 10 ** 10)
    for e in edge:
        ver[e[0]].append(e[1:])
    dist = {i: inf for i in range(N)}
    (dist[0], pq) = (0, [])
    heapq.heappush(pq, [dist[0], 0])
    while pq:
        (u_dis, u_node) = heapq.heappop(pq)
        if u_dis == dist[u_node]:
            for v in ver[u_node]:
                v_node = v[0]
                v_wei = v[1]
                if dist[u_node] + v_wei < dist[v_node]:
                    dist[v_node] = dist[u_node] + v_wei
                    heapq.heappush(pq, [dist[v_node], v_node])
    return -1 if dist[N - 1] == inf else dist[N - 1]
