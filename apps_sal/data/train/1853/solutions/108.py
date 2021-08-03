class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        # make graph
        dist = [[float('inf')] * n for _ in range(n)]

        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # use Floyd-Warshall Algorithm to find the minimum dist between any pair of nodes
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # in case there is a cycle, keep dist[i][j] as inf
                    if i == j:
                        continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # for all starting node, find their neihboring cities and return the one having fewest neighbors
        mn = n + 1
        output = None
        for start in range(n):
            count = len([d for d in dist[start] if d <= distanceThreshold])
            if count <= mn:
                mn = count
                output = start
        return output
