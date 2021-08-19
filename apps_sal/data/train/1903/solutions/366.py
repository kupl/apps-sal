class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        def dist(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((dist(points[i], points[j]), i, j))
        edges.sort()
        cost = 0
        # print(edges)
        parent = [i for i in range(n)]
        size = [1] * n

        def find(a):
            if parent[a] == a:
                p = a
            else:
                p = find(parent[a])
            parent[a] = p
            return p

        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa != pb:
                parent[pa] = pb
                size[pb] += size[pa]
                if size[pb] == n:
                    return True
            return False

        for e in edges:
            a, b = e[1], e[2]
            pa, pb = find(a), find(b)
            if pa != pb:
                cost += e[0]
                if (union(e[1], e[2])):
                    break
        return cost
