class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        A = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            A[i][i] = 0
        for x, y, w in edges:
            A[x][y] = w
            A[y][x] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j])

        res = -1
        val = float('inf')
        for i in range(n):
            t = sum([d <= distanceThreshold for d in A[i]])
            if t <= val:
                val = t
                res = i
        return res
