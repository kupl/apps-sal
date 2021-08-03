\"\"\"
DP bottom up time O(m*n) space O(m*n)
\"\"\"

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        \"\"\"
        snake tail originally at grid[0][0]
        mm[i][j][0] := steps to get to grid[i][j] in horizontal position
        mm[i][j][1] := steps to get to grid[i][j] in vertical position
        \"\"\"
        if len(grid) == 0: return 0  # no dungeon
        elif len(grid) == 1 and len(grid[0]) == 2: return 0

        n = len(grid)  # number of rows
        m = len(grid[0]) # number of columns
        mm = [[[math.inf, math.inf] for _ in range(m+1)] for _ in range(n+1)]
       
        for i in range(1, n+1):
            for j in range(1, m+1):
                ig = i-1
                jg = j-1
                if i==1 and j==1:
                    mm[1][1][0] = 0 # initial tail position
                else:
                    # move from up or left
                    if j<m and grid[ig][jg]==0 and grid[ig][jg+1]==0:
                        mm[i][j][0] = min(mm[i][j-1][0], mm[i-1][j][0])+1
                    # move from up or left
                    if i<n and grid[ig][jg]==0 and grid[ig+1][jg]==0:
                        mm[i][j][1] = min(mm[i][j-1][1], mm[i-1][j][1])+1
                # rotate
                if j<m and i<n and grid[ig][jg]==0 and grid[ig][jg+1]==0 and grid[ig+1][jg]==0 and grid[ig+1][jg+1]==0:
                    mm[i][j][0] = min(mm[i][j][0], mm[i][j][1]+1)
                    mm[i][j][1] = min(mm[i][j][1], mm[i][j][0]+1)
        if mm[n][m-1][0]==math.inf:
            return -1
        return mm[n][m-1][0]

