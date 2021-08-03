class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        parent = [i for i in range(l)]

        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]

        def union(a, b):
            p1 = find(a)
            p2 = find(b)
            parent[p2] = p1

        import heapq

        def new_cmp_lt(self, a, b):
            return a[0] - b[0]
        heapq.cmp_lt = new_cmp_lt
        res = 0

        p = []
        for i in range(l):
            for j in range(i + 1, l):
                p1 = points[i]
                p2 = points[j]
                d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                heapq.heappush(p, [d, i, j])
        while p:
            t = heapq.heappop(p)
            d = t[0]
            p1 = t[1]
            p2 = t[2]
            if find(p1) != find(p2):
                union(p1, p2)
                res += d
        return res
