class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def cost_of(i, j):
            (x1, y1) = points[i]
            (x2, y2) = points[j]
            return abs(x1 - x2) + abs(y1 - y2)
        N = len(points)
        parent = list(range(N))
        size = [1] * N

        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return False
            if size[x] < size[y]:
                (x, y) = (y, x)
            parent[y] = x
            size[x] += size[y]
            return True

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        edges = []
        for i in range(N):
            for j in range(i + 1, N):
                edges.append((cost_of(i, j), i, j))
        heapq.heapify(edges)
        total_cost = 0
        c = 0
        while edges:
            (cost, p1, p2) = heapq.heappop(edges)
            if union(p1, p2):
                c += 1
                total_cost += cost
                if c == N:
                    break
        return total_cost
