class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold: int) -> int:
        matrix = [[float('inf')]*n for _ in range(n)]
        for s, e, d in edges:
            matrix[s][e] = d
            matrix[e][s] = d
        for i in range(n):
            matrix[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])
        res, count = 0, n
        for i in range(n):
            tmp = sum(matrix[i][j] <= distanceThreshold for j in range(n))
            if tmp <= count:
                count = tmp
                res = i
        return res
