class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dp = [[0]*cols for _ in range(rows)]
        
        
        def g(x,y):
            nonlocal rows, cols
            if x < 0 or y < 0: return 0
            return dp[min(x,rows-1)][min(y,cols-1)]
        
        for i in range(rows):
            for j in range(cols):
                dp[i][j] = mat[i][j]+g(i-1,j)+g(i,j-1)-g(i-1,j-1)
        ans = [[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                ans[i][j] = g(i+K,j+K)+g(i-K-1,j-K-1)-g(i+K,j-K-1)-g(i-K-1,j+K)
        
        return ans

