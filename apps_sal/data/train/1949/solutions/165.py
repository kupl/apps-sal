class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def goDfsGo(row, col, bool_list):
            ret_max = 0
            bool_list[row][col] = False
            if row + 1 < len(grid) and bool_list[row + 1][col] == True and grid[row + 1][col] != 0:
                ret_max = max(ret_max, grid[row][col] + goDfsGo(row + 1, col, bool_list))

            if row - 1 >= 0 and bool_list[row - 1][col] == True and grid[row - 1][col] != 0:
                ret_max = max(ret_max, grid[row][col] + goDfsGo(row - 1, col, bool_list))

            if col + 1 < len(grid[0]) and bool_list[row][col + 1] == True and grid[row][col + 1] != 0:
                ret_max = max(ret_max, grid[row][col] + goDfsGo(row, col + 1, bool_list))

            if col - 1 >= 0 and bool_list[row][col - 1] == True and grid[row][col - 1] != 0:
                ret_max = max(ret_max, grid[row][col] + goDfsGo(row, col - 1, bool_list))

            bool_list[row][col] = True
            return max(ret_max, grid[row][col])

        mah_max = 0
        bool_list = [[True for i in range(len(grid[0]))] for i in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 0:
                    mah_max = max(mah_max, goDfsGo(row, col, bool_list))

        return mah_max
