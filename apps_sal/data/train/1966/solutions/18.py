class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        rows = []
        for row in mat:
            cur = [0]
            for x in row:
                cur.append(cur[-1] + x)
            rows.append(cur)
            
        res = 0
        for j2 in range(1, n+1):
            for j1 in range(j2):
                width = j2 - j1
                pre_idx = -1
                cur = 0
                for i in range(m):
                    if rows[i][j2] - rows[i][j1] != width:
                        pre_idx = i
                    else:
                        res += i - pre_idx
        return res

