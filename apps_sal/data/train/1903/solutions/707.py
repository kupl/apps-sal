class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parents = list(range(len(points)))

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                parents[py] = px
                return False
            return True
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        edges.sort()
        ans = 0
        for (w, x, y) in edges:
            if not union(x, y):
                ans += w
        return ans
