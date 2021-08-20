class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        mat = []
        for _ in range(n):
            mat.append([float('inf')] * n)
        for (i, j, d) in edges:
            mat[i][j] = d
            mat[j][i] = d
        for i in range(n):
            mat[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
        res = []
        for i in range(n):
            res.append(sum((1 for x in mat[i] if x <= distanceThreshold)))
        s = float('inf')
        for i in range(n):
            if res[i] <= s:
                s = res[i]
                out = i
        return out
