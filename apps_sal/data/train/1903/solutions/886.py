class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent = {}
        size = defaultdict(lambda: 1)

        def find(u):
            if u != parent.get(u, u):
                parent[u] = find(parent[u])  # path compression
            return parent.get(u, u)

        def union(u, v):
            u, v = find(u), find(v)
            if u != v:
                if size[u] < size[v]:  # union by size / rank
                    u, v = v, u

                parent[v] = u
                size[u] += size[v]

        total = 0
        edges = []
        n = len(points)
        for i in range(len(points)):
            for j in range(len(points)):
                if i!=j:
                    edges.append((abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),i,j))
        edges.sort()

        count = 0
        for cost, u, v in edges:
            if find(u) != find(v):
                total += cost
                count += 1
                union(u, v)
                if count == n-1:
                    return total

        return total
        

