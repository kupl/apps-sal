from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
\tdef findTheCityFloydWarshall(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
\t\tdist = [[float('inf')] * n for _ in range(n)]
\t\tfor u, v, w in edges:
\t\t\tdist[u][v] = dist[v][u] = w # bidirectional edges
\t\tfor i in range(n):
\t\t\tdist[i][i] = 0

\t\t# floyd-warshall
\t\tfor k in range(n):
\t\t\tfor i in range(n):
\t\t\t\tfor j in range(n):
\t\t\t\t\tdist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
\t\t
\t\tres = {sum(v <= distanceThreshold for v in dist[u]): u for u in range(n)}
\t\treturn res[min(res)]
\t
\tdef findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
\t\tgraph = defaultdict(list)
\t\tfor u, v, w in edges:
\t\t\tgraph[u].append((v, w))
\t\t\tgraph[v].append((u, w))

\t\tans = [float('inf'), float('inf')]

\t\tfor i in range(n):
\t\t\tpq = [(0, i)]
\t\t\tdist = [float('inf')] * n
\t\t\tdist[i] = 0
\t\t\tvisit = [False] * n

\t\t\twhile pq:
\t\t\t\tdist_u, u = heappop(pq)
\t\t\t\tvisit[i] = True
\t\t\t
\t\t\t\tfor v, w in graph[u]:
\t\t\t\t\tif not visit[v]:
\t\t\t\t\t\tif dist[v] > dist[u] + w:
\t\t\t\t\t\t\tdist[v] = dist[u] + w
\t\t\t\t\t\t\tif dist[v] <= distanceThreshold:
\t\t\t\t\t\t\t\theappush(pq, (dist[v], v))

\t\t\tcnt = 0
\t\t\tfor d in dist:
\t\t\t\tif d <= distanceThreshold: cnt += 1
\t\t\t
\t\t\tif cnt < ans[0]:
\t\t\t\tans = [cnt, i]
\t\t\telif cnt == ans[0]:
\t\t\t\tif i > ans[1]:
\t\t\t\t\tans = [cnt, i]
\t\t
\t\treturn ans[1]
