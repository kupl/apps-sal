class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        cache = {}
        for (i, coord) in enumerate(points):
            cache[i] = coord

        def compute(p1, p2):
            (x1, y1) = cache[p1]
            (x2, y2) = cache[p2]
            return abs(x1 - x2) + abs(y1 - y2)
        edges = []
        for (x, y) in combinations(list(cache.items()), 2):
            edges.append((compute(x[0], y[0]), x[0], y[0]))
        edges.sort(reverse=True)
        ans = 0
        L = len(cache)
        parents = list(range(L))

        def union(x, y):
            parents[find(x)] = find(y)

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        if L == 1:
            return 0
        while edges:
            (cost, n1, n2) = edges.pop()
            if find(n1) != find(n2):
                union(n1, n2)
                ans += cost
        return ans
