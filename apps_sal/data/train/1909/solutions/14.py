class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        
        up = [[0] * m for _ in range(n)]
        left = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    up[i][j] = 1 + up[i-1][j] if i > 0 else 1
                    left[i][j] = 1 + left[i][j-1] if j > 0 else 1
        
        max_len = 0
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if grid[i][j] == 1:
                    length = min(up[i][j], left[i][j])
                    for k in range(length-1, -1, -1):
                        if up[i][j-k] >= k+1 and left[i-k][j] >= k+1:
                            max_len = max(max_len, k+1)
        return max_len * max_len
