class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        
        res = 0
        dp = [[0 for _ in range(col)] for _ in range(row)]
        
        for i in range(row):
            for j in range(col-1, -1, -1):
                if mat[i][j] == 1:
                    dp[i][j] = mat[i][j]
                    if j < col-1:
                        dp[i][j] += dp[i][j+1]
        print(dp)                       
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    curr_row = i
                    width = dp[curr_row][j]
                    while curr_row < row and dp[curr_row][j] >= 1:
                        width = min(dp[curr_row][j], width)
                        res += width
                        curr_row +=1
        return res
                        
                                             

