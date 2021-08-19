class Solution:
    #     def minCostConnectPoints(self, points: List[List[int]]) -> int:
    #         n = len(points)
    #         if len(points) == 1: return 0
    #         res = 0
    #         curr = 0 # select a random point as the starting point
    #         dis = [math.inf] * n
    #         explored = set()

    #         for i in range(n - 1):
    #             x0, y0 = points[curr]
    #             explored.add(curr)
    #             for j, (x, y) in enumerate(points):
    #                 if j in explored: continue
    #                 dis[j] = min(dis[j], abs(x - x0) + abs(y - y0))

    #             delta, curr = min((d, j) for j, d in enumerate(dis))
    #             dis[curr] = math.inf
    #             res += delta

    #         return res
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        e = []
        for i, p1 in enumerate(points):
            for j in range(i + 1, n):
                p2 = points[j]
                w = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                e.append((i, j, w))
                e.append((j, i, w))
        parents = [i for i in range(n)]
        ranks = [1 for _ in range(n)]

        def find(x):
            while x != parents[x]:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if ranks[px] > ranks[py]:
                parents[py] = px
            elif ranks[px] < ranks[py]:
                parents[px] = py
            else:
                parents[py] = px
                ranks[px] += 1
            return True
        res = 0
        for u, v, w in sorted(e, key=lambda x: x[2]):
            if not union(u, v):
                continue
            else:
                res += w
        return res
