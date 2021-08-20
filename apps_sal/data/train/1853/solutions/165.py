class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = collections.defaultdict(dict)
        for (a, b, c) in edges:
            adj[a][b] = adj[b][a] = c

        def bfs(s, distanceThreshold):
            visited = [False] * n
            dist = [float('inf')] * n
            frontier = [(0, s)]
            while not all(visited) and frontier:
                (d, s) = heapq.heappop(frontier)
                if d > distanceThreshold:
                    break
                dist[s] = d
                visited[s] = True
                for t in adj[s]:
                    if not visited[t]:
                        heapq.heappush(frontier, (d + adj[s][t], t))
            return len([d for d in dist if d <= distanceThreshold])
        res = 0
        count = n
        for i in range(n):
            c = bfs(i, distanceThreshold)
            if c <= count:
                res = max(res, i)
                count = c
        return res
