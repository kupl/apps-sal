class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        
        dp = [[0 for _ in range(col)] for _ in range(row)]
        
        # find the length of the left rec at point(i, j)
        for i in range(row):
            for j in range(col):
                if mat[i][j]:
                    dp[i][j] = dp[i][j-1] + 1 if j >= 1 else 1
        
        # from the right end (i,j) = (row_end, col_end) to find height = 1,2...
        res = 0
        for i in range(row):
            for j in range(col):
                leftnum = float(\"inf\")
                for k in range(i, -1, -1):
                    leftnum = min(leftnum, dp[k][j])
                    
                    if leftnum == 0:
                        break
                    res += leftnum
                    
        return res
