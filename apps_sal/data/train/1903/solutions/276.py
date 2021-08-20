class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        dMat = [[-1 for j in range(n)] for i in range(n)]

        def d(p1, p2):
            (a, b) = p1
            (c, d) = p2
            return abs(a - c) + abs(b - d)
        for (i, p1) in enumerate(points):
            for (j, p2) in enumerate(points):
                dMat[i][j] = d(p1, p2)
        key = [float('inf')] * n
        parent = [None] * n
        key[0] = 0
        mstSet = [False] * n
        parent[0] = -1

        def minKey():
            min = float('inf')
            for v in range(n):
                if key[v] < min and mstSet[v] == False:
                    min = key[v]
                    min_index = v
            return min_index
        for cout in range(n):
            u = minKey()
            mstSet[u] = True
            for v in range(n):
                if dMat[u][v] > 0 and mstSet[v] == False and (key[v] > dMat[u][v]):
                    key[v] = dMat[u][v]
                    parent[v] = u
        res = 0
        for v in range(n):
            if parent[v] != -1:
                u = parent[v]
                res += dMat[u][v]
        return res
