class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        p = []
        for i in range(m):
            row = [0]
            s = 0
            for j in range(n):
                s += mat[i][j]
                row.append(s)
            p.append(row)
        
        ans = []
        for i in range(m):
            row = []
            for j in range(n):
                s = 0
                top = max(0, i - k)
                bottom = min(m, i + k + 1)
                for g in range(top, bottom):
                    left = max(0, j - k)
                    right = min(n, j + k + 1)
                    s += p[g][right] - p[g][left]
                row.append(s)
            ans.append(row)
        return ans

