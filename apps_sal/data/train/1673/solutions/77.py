\"\"\"


dp[r][c] = the minimum sum of falling int to row r and column c

dp[r][c] = arr[r][c] + min(dp[r-1][pc] for all pc != c)

\"\"\"



class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        rows = len(arr)
        cols = len(arr[0])
        infi = float('inf')
        dp = [[infi]*cols for _ in range(rows)]
        for c in range(cols):
            dp[0][c] = arr[0][c]
            
        for r in range(1, rows):
            for c in range(cols):
                dp[r][c] = arr[r][c] + min(dp[r-1][pc] for pc in range(cols) if pc != c)
        return min(dp[-1])    
                    
