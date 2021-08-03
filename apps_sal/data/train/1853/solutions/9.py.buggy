from typing import List
from collections import defaultdict

class Solution:
\tdef findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
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
\t\tprint(dist)

\t\tres = {sum(v <= distanceThreshold for v in dist[u]): u for u in range(n)}
\t\t
\t\treturn res[min(res)]
