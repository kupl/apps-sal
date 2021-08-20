class Solution:

    def minCostConnectPoints(self, p: List[List[int]]) -> int:
        n = len(p)
        parents = list(range(n))

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            r1 = find(x)
            r2 = find(y)
            if r1 != r2:
                parents[r2] = r1
                return True
            else:
                return False

        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        a = []
        for i in range(n):
            for j in range(i + 1, n):
                d = dist(p[i], p[j])
                a.append((d, i, j))
        a.sort()
        ans = 0
        for (d, p1, p2) in a:
            if union(p1, p2):
                ans += d
        return ans
