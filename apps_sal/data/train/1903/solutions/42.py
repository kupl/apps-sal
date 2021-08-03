class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        n = len(points)
        fa = [i for i in range(n)]

        def findfa(x):
            if fa[x] == x:
                return x
            else:
                fa[x] = findfa(fa[x])
                return fa[x]
        e = [(dist(i, j), i, j) for j in range(n) for i in range(n)]
        e.sort()
        ans = 0
        for edge in e:
            if findfa(edge[1]) != findfa(edge[2]):
                ans += edge[0]
                fa[findfa(edge[1])] = findfa(edge[2])
        return ans
