class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        L = [[[float('inf') for i in range(n + 1)] for j in range(n)] for k in range(n)]
        for (u, v, w) in edges:
            L[u][v][0] = w
            L[v][u][0] = w
        for k in range(1, n + 1):
            for i in range(n):
                for j in range(n):
                    if j == i:
                        continue
                    L[i][j][k] = min(L[i][j][k - 1], L[i][k - 1][k - 1] + L[k - 1][j][k - 1])
        min_ct = float('inf')
        minval = n - 1
        for i in range(n - 1, -1, -1):
            ct = 0
            for j in range(n):
                if i == j:
                    continue
                if L[i][j][n] <= distanceThreshold:
                    ct += 1
            if ct < min_ct:
                min_ct = ct
                minval = i
        return minval
