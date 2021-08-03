class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = list(range(n))

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            tx = find(x)
            ty = find(y)
            if tx != ty:
                uf[tx] = ty

        def l1dist(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])

        dist = []
        for i in range(n):
            for j in range(i + 1, n):
                dist.append((l1dist(points[i], points[j]), i, j))

        dist.sort()
        ans = 0
        cnt = 0
        for d, x, y in dist:
            if cnt == n:
                break
            if find(x) != find(y):
                union(x, y)
                ans += d
                cnt += 1
        return ans
