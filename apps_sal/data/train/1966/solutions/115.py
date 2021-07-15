class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        cumones = [[0]*m for x in range(n)]
        for i in range(n):
            for j in range(m-1, -1, -1):
                if mat[i][j] == 1:
                    cumones[i][j] = 1+(cumones[i][j+1] if j < m-1 else 0)
        ct = 0
        for i in range(n):
            for j in range(m):
                minw = sys.maxsize
                for k in range(i,n):
                    if mat[i][j] == 1:
                        minw = min(minw, cumones[k][j])
                        ct += minw
        return ct
