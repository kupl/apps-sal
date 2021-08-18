class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0

        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        n = len(points)
        parents = list(range(n))

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parents[py] = px
                return True
            return False
        ans = 0
        count = 0
        g = []
        for i in range(n):
            for j in range(i + 1, n):
                cost = distance(points[i], points[j])
                g.append([cost, i, j])
        for cost, pt1, pt2 in sorted(g):
            if union(pt1, pt2):
                ans += cost
                count += 1
            if count == n - 1:
                return ans
