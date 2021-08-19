class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        q = [(0, 0)]
        visited = set()
        G = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i != j:
                    (xi, yi) = points[i]
                    (xj, yj) = points[j]
                    cost = abs(xi - xj) + abs(yi - yj)
                    G[i].append((cost, j))
                    G[j].append((cost, i))
        total = 0
        while q and len(visited) < n:
            (cost1, v1) = heappop(q)
            if v1 not in visited:
                visited.add(v1)
                total += cost1
                for (cost2, v2) in G[v1]:
                    heappush(q, (cost2, v2))
        return total
