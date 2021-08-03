class Solution:
    def get_sum(self, grid, x, y, sum_, all_grids):
        if [x, y] not in all_grids and not grid[x][y] == 0:
            sum_ = sum_ + grid[x][y]
            all_grids.append([x, y])

            sum_top, sum_bottom, sum_left, sum_right = sum_, sum_, sum_, sum_
            if x > 0:
                sum_top = self.get_sum(grid, x - 1, y, sum_, all_grids.copy())
            if x < len(grid) - 1:
                sum_bottom = self.get_sum(grid, x + 1, y, sum_, all_grids.copy())
            if y > 0:
                sum_left = self.get_sum(grid, x, y - 1, sum_, all_grids.copy())
            if y < len(grid[0]) - 1:
                sum_right = self.get_sum(grid, x, y + 1, sum_, all_grids.copy())

            return max(sum_top, sum_bottom, sum_left, sum_right)

        else:
            return sum_

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        sums = []
        for m in range(len(grid)):
            for n in range(len(grid[m])):
                sums.append(self.get_sum(grid, m, n, 0, []))

        return max(sums)
