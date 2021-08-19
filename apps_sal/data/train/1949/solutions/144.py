class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def goDfsGo(row, col):
            ret_max = 0
            temp_val = grid[row][col]
            grid[row][col] = False
            if row + 1 < len(grid) and grid[row + 1][col] != False and grid[row + 1][col] != 0:
                ret_max = max(ret_max, temp_val + goDfsGo(row + 1, col))

            if row - 1 >= 0 and grid[row - 1][col] != False and grid[row - 1][col] != 0:
                ret_max = max(ret_max, temp_val + goDfsGo(row - 1, col))

            if col + 1 < len(grid[0]) and grid[row][col + 1] != False and grid[row][col + 1] != 0:
                ret_max = max(ret_max, temp_val + goDfsGo(row, col + 1))

            if col - 1 >= 0 and grid[row][col - 1] != False and grid[row][col - 1] != 0:
                ret_max = max(ret_max, temp_val + goDfsGo(row, col - 1))

            grid[row][col] = temp_val
            return max(ret_max, grid[row][col])

        mah_max = 0
        #bool_list=[[True for i in range(len(grid[0]))] for i in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 0:
                    mah_max = max(mah_max, goDfsGo(row, col))
                    # print(mah_max)

        return mah_max
