class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        costs = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                costs[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                costs[j][i] = costs[i][j]
        parent = [-1 for _ in range(n)]
        keyval = [-1 for _ in range(n)]
        mst = [False for _ in range(n)]
        keyval[0] = 0
        for i in range(n):
            mini = -1
            u = -1
            for j in range(n):
                if mst[j]:
                    continue
                if keyval[j] == -1:
                    continue
                if mini == -1:
                    mini = keyval[j]
                    u = j
                elif mini != -1 and mini > keyval[j]:
                    mini = keyval[j]
                    u = j
            mst[u] = True
            for j in range(n):
                if j != u and (not mst[j]):
                    if keyval[j] == -1 or keyval[j] > costs[u][j]:
                        keyval[j] = costs[u][j]
                        parent[j] = u
        r = 0
        for i in range(1, n):
            r += costs[parent[i]][i]
        return r
