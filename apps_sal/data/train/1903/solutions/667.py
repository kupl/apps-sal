class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ok = [-1 for i in range(len(points))]

        def union(x, y):
            x1 = find(x)
            x2 = find(y)
            ok[x1] = x2

        def find(x):
            if ok[x] == -1:
                return x
            else:
                ok[x] = find(ok[x])
                return ok[x]
        d = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d.append([abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j])
        d.sort()
        ans = 0
        for i in d:
            x = find(i[1])
            y = find(i[2])
            if x != y:
                union(i[1], i[2])
                ans += i[0]
        return ans
