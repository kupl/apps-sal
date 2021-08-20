class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def minnode(n, keyval, mstset):
            mini = 999999999999
            mini_index = None
            for i in range(n):
                if mstset[i] == False and keyval[i] < mini:
                    mini = keyval[i]
                    mini_index = i
            return mini_index

        def findcost(n, city):
            parent = [None] * n
            keyval = [None] * n
            mstset = [None] * n
            for i in range(n):
                keyval[i] = 9999999999999
                mstset[i] = False
            parent[0] = -1
            keyval[0] = 0
            for i in range(n - 1):
                u = minnode(n, keyval, mstset)
                mstset[u] = True
                for v in range(n):
                    if city[u][v] and mstset[v] == False and (city[u][v] < keyval[v]):
                        keyval[v] = city[u][v]
                        parent[v] = u
            cost = 0
            for i in range(1, n):
                cost += city[parent[i]][i]
            return cost
        n = len(points)
        city = [[0 for c in range(n)] for r in range(n)]
        for r in range(n):
            c1 = points[r]
            for c in range(n):
                c2 = points[c]
                val = abs(points[r][0] - points[c][0]) + abs(points[r][1] - points[c][1])
                city[r][c] = val
        return findcost(n, city)
