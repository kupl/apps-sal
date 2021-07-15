class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        R = len(mat)
        C = len(mat[0])
        dp = [[None for i in range(C)] for j in range(R)]
        
        for i in range(R):
            count = 0
            for j in range(C-1,-1, -1):
                if mat[i][j] == 1:
                    count += 1
                else:
                    count = 0
                dp[i][j] = count
        
        result = 0
        for i in range(R):
            for j in range(C):
                mn = float(\"inf\")
                for k in range(i, R):
                    mn = min(mn, dp[k][j])
                    result += mn
        
        return result

