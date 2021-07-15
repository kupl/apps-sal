class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max = 0
        hor = [[0] * m for _ in range(n)]
        ver = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    hor[i][j] = hor[i][j-1] + 1 if j > 0 else 1
                    ver[i][j] = ver[i-1][j] + 1 if i > 0 else 1
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                small = min(ver[i][j], hor[i][j])
                while small > max:
                    if hor[i-small+1][j] >= small and ver[i][j-small+1] >= small:
                        max = small
                        break
                    small -= 1
        return max**2

