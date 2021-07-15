class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        # check discussion
        # Time: O(N^3)
        # Step1: Need two auxillary matrix to record the number of consecutive 1s on the vertical and horizontal direction
        # Step2: check every possible candidate width from min(m, n) to 1
        
        m, n = len(grid), len(grid[0])
        # Key: initialize them to SAME as grid, because value=0 got length 0, value=1 got length 1
        horizontal_len = [row[:] for row in grid]
        vertical_len = [row[:] for row in grid]
        # calculate maximum length of one in two directions
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    if i > 0:
                        vertical_len[i][j] = vertical_len[i - 1][j] + 1
                    if j > 0:
                        horizontal_len[i][j] = horizontal_len[i][j - 1] + 1
        
        for width in range(min(m, n), 0, -1):
            for i in range(m - width + 1):
                for j in range(n - width + 1):
                    # Key: check the length on the 4 vertex in the horizontal/vertical direction, which indicate the maximum length
                    valid_width = min(horizontal_len[i][j + width - 1],
                                     horizontal_len[i + width - 1][j + width - 1],
                                     vertical_len[i + width - 1][j],
                                     vertical_len[i + width - 1][j + width - 1])
                    # Key: NOT return valid_width, because \"width\" is the currently checking width, while valid_width MIGHT misleading. grid=[[0,1,0,1],[1,1,1,1],[1,1,0,1],[1,1,1,1]], i=1,j=1, valid_width is 4, but TRUE valid width is ONLY 3. If TRUR width is 4, we SHOULD find it when i=0,j=0
                    if valid_width >= width:
                        return width ** 2
        return 0

